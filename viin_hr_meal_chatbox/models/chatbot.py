from odoo import models, fields
import requests
import json

class Chatbot(models.Model):
    _name = 'chat.bot'
    _description = 'Chatbot'
        
    def _apply_logic(self, record, values, command=None):
            chatbot_id = self.env['ir.model.data']._xmlid_to_res_id("viin_hr_meal_chatbox.chatbot_partner")
            if len(record) != 1 or values.get("author_id") == chatbot_id:
                return
            if self._is_bot_pinged(values) or self._is_bot_in_chat_channel(record):
                body = values.get("body", "").replace(u'\xa0', u' ').strip().lower().strip(".!")
                answer = self._get_answer(record, body, values, command)
                if answer:
                    message_type = values.get('message_type', 'comment')
                    subtype_id = values.get('subtype_id', self.env['ir.model.data']._xmlid_to_res_id('mail.mt_comment'))
                    record.with_context(mail_create_nosubscribe=True).sudo().message_post(body=answer, author_id=chatbot_id, message_type=message_type, subtype_id=subtype_id)
    
    def _get_answer(self, record, body, values, command=False):
        # onboarding
        headers = {
            "Content-Type": "application/json",
        }
        payload ={
                "message": body
                }
        response = requests.post('http://localhost:5005/webhooks/rest/webhook?token={auth_token}', data=json.dumps(payload), headers=headers)
        data = response.json()
        return data[0]['text']
        
        
    def _is_bot_pinged(self, values):
        chatbot_id = self.env['ir.model.data']._xmlid_to_res_id("viin_hr_meal_chatbox.chatbot_partner")
        return chatbot_id in values.get('partner_ids', [])

    def _is_bot_in_chat_channel(self, record):
        chatbot_id = self.env['ir.model.data']._xmlid_to_res_id("viin_hr_meal_chatbox.chatbot_partner")
        if record._name == 'mail.channel' and record.channel_type == 'chat':
            return chatbot_id in record.with_context(active_test=False).channel_partner_ids.ids
        return False
