# Chatbot_meal-to-Odoo

#Tổng quan về chatbot:
  Trước khi xây dựng 1 chatbot cho doanh nghiệp, nhà lãnh đạo cần trả lời các câu hỏi để xác định phạm vi cũng như mục tiêu hướng tới: https://medium.com/@thebabar/7-questions-business-leaders-must-ask-before-starting-on-a-conversational-ai-system-d3642e825c05
  
  Chatbot được xây dựng trên 1 trong 2 mô hình chính: https://medium.com/voice-tech-podcast/types-of-chatbot-technology-72d095df2540
  - Mô hình ngôn ngữ: Cứng ngắc, khó phát triển, dựa trên nguyên tắc if/then - phổ biến đang tg tác
  - Mô hình học máy( AI Chatbots): Yêu cầu dữ liệu lớn, chính xác, khó can thiệp, tối ưu hóa, cải thiện
  - Mô hình kết hợp: tận dụng được ưu điểm của 2 mô hình
  
 Các cách để làm chatbot: https://miai.vn/2019/09/03/rasa-series-1-ai-cung-co-the-lam-chatbot-sieu-ngon-khong-lo/
	- Kiểu if then theo câu: dễ làm, đơn giản, chỉ trả lời y hệt câu đầu vào.
	- Kiểu rule base chatbot có xử lý ngôn ngữ tự nhiên và áp dụng mạng NN để xác định KH muốn gì và tìm câu trả lời phù hợp: định nghĩa mẫu câu đầu vào và các câu trả lời, hỏi khác mẫu câu vẫn trả lời đc.
  VD: RASA,.... 25 nền tảng chatbot: https://medium.com/chatbots-journal/25-chatbot-platforms-a-comparative-table-aeefc932eaff
	- Kiểu generation based chatbot: sau khi được train lien tục câu hỏi và câu trả lời thì bot có khả năng tự sinh ra câu trả lời ứng với nội dung KH chat( không cần định nghĩa). Tuy nhiên thực tế triển khai thì khó kiểm soát được câu trả lời của bot: ngô nghê, đôi khi có nội dung nhạy cảm.
  VD: Chatbot mới ra của Meta: BlenderBot 3: https://ai.facebook.com/blog/blenderbot-3-a-175b-parameter-publicly-available-chatbot-that-improves-its-skills-and-safety-over-time/
  nói xấu ông chủ của mình: https://www.google.com/search?q=nh%E1%BA%ADn+%C4%91%E1%BB%8Bnh+chat+bot+m%E1%BB%9Bi+ra+c%E1%BB%A7a+meta&oq=nh%E1%BA%ADn+%C4%91%E1%BB%8Bnh+chat+bot+m%E1%BB%9Bi+ra+c%E1%BB%A7a+meta&aqs=chrome..69i57.8468j1j7&sourceid=chrome&ie=UTF-8
  
  Do đó, hiện nay loại số 2 vẫn được dùng nhiều nhất vì cân bằng giữa độ mềm dẻo trong giao tiếp, lại kiểm soát được thông tin
