# -*- coding: utf-8 -*-
"""Sinh data/ktvm.json từ ngân hàng câu hỏi bên dưới.

Chạy:  python tools/build_questions.py

M(...) = trắc nghiệm 4 đáp án — đáp án đúng luôn viết ở vị trí ĐẦU TIÊN,
         script tự xáo vị trí (seed cố định nên kết quả ổn định giữa các lần chạy).
T(...) = nhận định Đúng/Sai kèm giải thích.
"""
import json
import random
from pathlib import Path

C1 = "Chương 1"
C2 = "Chương 2"
C3 = "Chương 3"
SRC = {
    C1: "Chương 1 – Giới thiệu về kinh tế học vĩ mô",
    C2: "Chương 2 – Dữ liệu kinh tế vĩ mô",
    C3: "Chương 3 – Sản xuất và tăng trưởng",
}

BANK = []


def M(ch, question, options, why, slide):
    BANK.append(("mcq", ch, question, options, why, slide))


def T(ch, statement, is_true, why, slide):
    BANK.append(("tf", ch, statement, is_true, why, slide))


# ───────────────────────── CHƯƠNG 1 ─────────────────────────
M(C1, "Kinh tế học là môn khoa học xã hội nghiên cứu điều gì?",
  ["Cách xã hội sử dụng các nguồn lực có hạn để đáp ứng nhu cầu của con người",
   "Cách doanh nghiệp tối đa hóa lợi nhuận bằng mọi giá",
   "Cách chính phủ in tiền để tài trợ chi tiêu",
   "Cách tạo ra nguồn lực vô hạn cho xã hội"],
  "Định nghĩa trong bài: kinh tế học nghiên cứu cách xã hội sử dụng nguồn lực KHAN HIẾM (có hạn) để đáp ứng nhu cầu con người. "
  "Các phương án khác chỉ là một khía cạnh hẹp (lợi nhuận DN, in tiền) hoặc sai bản chất (nguồn lực không bao giờ vô hạn).", 4)

M(C1, "Yếu tố nào sau đây KHÔNG thuộc nhóm các yếu tố sản xuất được nêu trong bài?",
  ["Tiền mặt dự trữ trong két của hộ gia đình",
   "Lao động (L)",
   "Tư bản (K)",
   "Công nghệ"],
  "Các yếu tố sản xuất gồm: lao động, tài nguyên thiên nhiên, tư bản và công nghệ — là đầu vào để sản xuất hàng hóa, dịch vụ. "
  "Tiền mặt cất trữ không trực tiếp tham gia sản xuất nên không phải yếu tố sản xuất.", 5)

M(C1, "Theo bài giảng, \"Mười nguyên lý của kinh tế học\" được chia thành ba nhóm câu hỏi nào?",
  ["Con người ra quyết định thế nào; con người tương tác thế nào; nền kinh tế vận hành thế nào",
   "Sản xuất cái gì; sản xuất thế nào; sản xuất cho ai",
   "Cung; cầu; giá cả",
   "Tiêu dùng; đầu tư; chi tiêu chính phủ"],
  "Bài chia 10 nguyên lý thành 3 nhóm: ra quyết định (1–4), tương tác (5–7), vận hành của nền kinh tế (8–10). "
  "\"Sản xuất cái gì, thế nào, cho ai\" là ba vấn đề kinh tế cơ bản, không phải cách phân nhóm 10 nguyên lý; C, I, G là thành phần GDP.", 6)

M(C1, "Nguyên lý \"Con người đối mặt với sự đánh đổi\" thuộc nhóm nào?",
  ["Con người ra quyết định như thế nào",
   "Con người tương tác với nhau như thế nào",
   "Nền kinh tế vận hành như thế nào",
   "Vai trò của chính phủ trong thị trường"],
  "Nguyên lý 1–4 (đánh đổi, chi phí cơ hội, suy nghĩ tại điểm cận biên, phản ứng với khuyến khích) đều thuộc nhóm \"Con người ra quyết định như thế nào\".", 7)

M(C1, "\"Chi phí của một thứ là cái mà bạn từ bỏ để có được nó\" mô tả khái niệm nào?",
  ["Chi phí cơ hội",
   "Chi phí kế toán",
   "Chi phí cận biên của doanh nghiệp",
   "Chi phí chìm"],
  "Cái bị từ bỏ để có được một thứ chính là chi phí cơ hội (nguyên lý 2). Chi phí kế toán chỉ tính khoản chi bằng tiền; chi phí chìm là khoản đã bỏ ra không thu hồi được; chi phí cận biên là chi phí của thêm một đơn vị.", 7)

M(C1, "Nguyên lý \"Thương mại có thể làm cho mọi người đều được lợi\" thuộc nhóm nào?",
  ["Con người tương tác với nhau như thế nào",
   "Con người ra quyết định như thế nào",
   "Nền kinh tế vận hành như thế nào",
   "Nguyên lý về lạm phát"],
  "Nguyên lý 5 (thương mại), 6 (thị trường là phương thức tốt) và 7 (chính phủ đôi khi cải thiện kết cục thị trường) thuộc nhóm \"tương tác\".", 8)

M(C1, "Nguyên lý nào sau đây thuộc nhóm \"Nền kinh tế vận hành như thế nào\"?",
  ["Giá cả tăng khi chính phủ in quá nhiều tiền",
   "Con người phản ứng với các động cơ khuyến khích",
   "Thị trường thường là một phương thức tốt để tổ chức hoạt động kinh tế",
   "Con người duy lý suy nghĩ tại điểm cận biên"],
  "Nhóm \"vận hành\" gồm nguyên lý 8 (mức sống phụ thuộc năng lực sản xuất), 9 (in nhiều tiền → giá tăng), 10 (đánh đổi ngắn hạn lạm phát – thất nghiệp). "
  "Các phương án còn lại thuộc nhóm ra quyết định hoặc tương tác.", 9)

M(C1, "Theo mười nguyên lý, mức sống của một nước phụ thuộc chủ yếu vào điều gì?",
  ["Năng lực sản xuất hàng hóa và dịch vụ của nước đó",
   "Lượng tiền chính phủ in ra",
   "Diện tích lãnh thổ của quốc gia",
   "Số lượng người tiêu dùng trong nước"],
  "Nguyên lý 8: mức sống phụ thuộc vào năng lực sản xuất (năng suất). In nhiều tiền chỉ gây lạm phát (nguyên lý 9); diện tích hay số dân không quyết định mức sống.", 9)

M(C1, "Trong ngắn hạn, xã hội đối mặt với sự đánh đổi giữa hai biến số nào?",
  ["Lạm phát và thất nghiệp",
   "Tiết kiệm và đầu tư",
   "Xuất khẩu và nhập khẩu",
   "GDP và GNP"],
  "Nguyên lý 10: xã hội đối mặt với đánh đổi ngắn hạn giữa lạm phát và thất nghiệp (giảm lạm phát thường kéo theo thất nghiệp tạm thời tăng).", 9)

M(C1, "Trong sơ đồ chu chuyển, hộ gia đình đóng vai trò gì trên thị trường các yếu tố sản xuất?",
  ["Người bán (cung cấp lao động, đất đai, vốn)",
   "Người mua lao động, đất đai và vốn",
   "Người bán hàng hóa và dịch vụ",
   "Không tham gia thị trường này"],
  "Hộ gia đình sở hữu và bán các yếu tố sản xuất cho doanh nghiệp, nhận lại lương, tiền thuê, lợi nhuận. Doanh nghiệp mới là người mua yếu tố sản xuất và là người bán hàng hóa, dịch vụ.", 12)

M(C1, "Trong sơ đồ chu chuyển, dòng \"lương, tiền thuê và lợi nhuận\" chảy theo chiều nào?",
  ["Từ doanh nghiệp đến hộ gia đình qua thị trường các yếu tố sản xuất",
   "Từ hộ gia đình đến doanh nghiệp qua thị trường hàng hóa và dịch vụ",
   "Từ chính phủ đến doanh nghiệp",
   "Từ hộ gia đình đến doanh nghiệp qua thị trường các yếu tố sản xuất"],
  "Doanh nghiệp trả lương, tiền thuê, lợi nhuận cho hộ gia đình để mua các yếu tố sản xuất; với hộ gia đình đây là thu nhập. Dòng từ hộ gia đình đến doanh nghiệp là chi tiêu mua hàng hóa, dịch vụ.", 12)

M(C1, "Một điểm nằm BÊN TRONG đường giới hạn khả năng sản xuất (PPF) thể hiện điều gì?",
  ["Nền kinh tế đang sản xuất không hiệu quả",
   "Nền kinh tế sản xuất hiệu quả",
   "Mức sản lượng không thể đạt được với nguồn lực hiện có",
   "Nền kinh tế đang tăng trưởng"],
  "Điểm nằm trên PPF là hiệu quả; điểm bên trong là chưa tận dụng hết nguồn lực (không hiệu quả); điểm bên ngoài là không thể đạt được với nguồn lực và công nghệ hiện tại. Tăng trưởng thể hiện bằng PPF dịch ra ngoài.", 13)

M(C1, "Yếu tố nào làm đường PPF dịch chuyển ra ngoài?",
  ["Tiến bộ công nghệ",
   "Thất nghiệp gia tăng",
   "Chuyển nguồn lực từ sản xuất ô tô sang máy tính",
   "Giá hàng hóa tăng"],
  "Theo bài, PPF dịch ra ngoài nhờ tăng trưởng kinh tế, cụ thể do tích lũy tư bản và tiến bộ công nghệ. Thất nghiệp đưa nền kinh tế vào bên trong PPF; chuyển nguồn lực giữa hai ngành chỉ là di chuyển dọc theo PPF.", 16)

M(C1, "Khái niệm nào sau đây KHÔNG được minh họa trực tiếp bằng đường PPF?",
  ["Lạm phát",
   "Sự đánh đổi",
   "Chi phí cơ hội",
   "Tăng trưởng kinh tế"],
  "PPF minh họa: hiệu quả, sự đánh đổi, chi phí cơ hội và tăng trưởng kinh tế. PPF đo lượng hàng hóa thực, không chứa thông tin về mức giá nên không thể hiện lạm phát.", 15)

M(C1, "Nội dung nào thuộc phạm vi nghiên cứu của kinh tế học VĨ MÔ?",
  ["Tác động của vay nợ chính phủ đến tăng trưởng kinh tế cả nước",
   "Ảnh hưởng của giá thịt đến lượng mua của một hộ gia đình",
   "Quyết định thuê thêm nhân viên của một cửa hàng",
   "Giá kem trên một thị trường cụ thể"],
  "Kinh tế vĩ mô nghiên cứu nền kinh tế như một tổng thể (tăng trưởng, lạm phát, thất nghiệp, chính sách quốc gia). Các phương án còn lại xem xét đơn vị kinh tế cá biệt hoặc thị trường cụ thể — thuộc kinh tế vi mô.", 17)

M(C1, "Phát biểu nào sau đây là phát biểu CHUẨN TẮC?",
  ["Chính phủ nên tăng lương tối thiểu",
   "Tăng lương tối thiểu làm tăng thất nghiệp ở lao động trẻ",
   "Năm ngoái tỷ lệ lạm phát là 4%",
   "Khi giá tăng, lượng cầu giảm"],
  "Phân tích chuẩn tắc chỉ ra sự việc NÊN diễn ra thế nào (có chữ \"nên\", mang tính giá trị). Các phương án còn lại mô tả thế giới như nó vốn có, có thể kiểm chứng bằng dữ liệu → thực chứng.", 18)

M(C1, "Thị trường cạnh tranh là thị trường có đặc điểm gì?",
  ["Nhiều người mua và người bán, mỗi người không có khả năng ảnh hưởng đến giá thị trường",
   "Chỉ có một người bán quyết định giá",
   "Có ít người bán và họ phối hợp với nhau để định giá",
   "Giá do chính phủ ấn định"],
  "Định nghĩa trong bài: thị trường cạnh tranh có nhiều người bán và mua, mỗi người không đủ sức tác động đến giá. Một người bán là độc quyền; ít người bán phối hợp là cartel/độc quyền nhóm.", 20)

M(C1, "Tại mức giá thị trường làm cho lượng cung bằng lượng cầu, ta gọi đó là:",
  ["Điểm cân bằng",
   "Điểm dư thừa",
   "Điểm thiếu hụt",
   "Điểm giới hạn khả năng sản xuất"],
  "Điểm cân bằng là tình huống giá thị trường làm lượng cung bằng lượng cầu; mức giá đó là giá cân bằng, lượng tương ứng là sản lượng cân bằng. Dư thừa (cung > cầu) và thiếu hụt (cầu > cung) xảy ra khi giá lệch khỏi cân bằng.", 28)

T(C1, "Kinh tế học nghiên cứu cách xã hội quản lý các nguồn lực khan hiếm (có hạn).", True,
  "ĐÚNG. Đây chính là định nghĩa kinh tế học trong bài: khoa học xã hội nghiên cứu cách xã hội sử dụng nguồn lực có hạn nhằm đáp ứng nhu cầu con người.", 4)

T(C1, "Con người duy lý ra quyết định bằng cách so sánh lợi ích cận biên và chi phí cận biên.", True,
  "ĐÚNG. Nguyên lý 3: con người duy lý suy nghĩ tại điểm cận biên — chỉ thực hiện thêm một hoạt động khi lợi ích tăng thêm lớn hơn chi phí tăng thêm.", 7)

T(C1, "Thương mại giữa hai quốc gia luôn là trò chơi có tổng bằng 0: một nước được thì nước kia mất.", False,
  "SAI. Nguyên lý 5 khẳng định thương mại có thể làm cho MỌI bên đều được lợi, vì cho phép mỗi bên chuyên môn hóa vào việc mình làm tốt nhất và trao đổi để có nhiều hàng hóa, dịch vụ hơn.", 8)

T(C1, "Theo mười nguyên lý của kinh tế học, chính phủ không bao giờ có thể cải thiện được kết cục thị trường.", False,
  "SAI. Nguyên lý 7: ĐÔI KHI chính phủ có thể cải thiện kết cục thị trường (ví dụ khi có thất bại thị trường như ngoại tác, quyền lực thị trường). Thị trường thường là tốt (nguyên lý 6) nhưng không phải lúc nào cũng hoàn hảo.", 8)

T(C1, "Theo mười nguyên lý, giá cả tăng khi chính phủ in quá nhiều tiền.", True,
  "ĐÚNG. Nguyên lý 9: khi chính phủ in quá nhiều tiền, giá trị của tiền giảm và mức giá chung tăng — tức lạm phát.", 9)

T(C1, "Nhà kinh tế học sử dụng các giả định để đơn giản hóa vấn đề phức tạp, giúp dễ hiểu hơn.", True,
  "ĐÚNG. Với tư cách nhà khoa học, nhà kinh tế dùng giả định và mô hình (sơ đồ chu chuyển, PPF) để giải thích thế giới; giả định giúp đơn giản hóa vấn đề phức tạp.", 11)

T(C1, "Trong sơ đồ chu chuyển, doanh nghiệp là người bán trên thị trường các yếu tố sản xuất.", False,
  "SAI. Trên thị trường các yếu tố sản xuất, doanh nghiệp là người MUA (thuê lao động, đất đai, vốn); hộ gia đình mới là người bán. Doanh nghiệp là người bán trên thị trường hàng hóa và dịch vụ.", 12)

T(C1, "Một điểm nằm bên ngoài đường PPF là mức sản lượng không thể đạt được với nguồn lực và công nghệ hiện có.", True,
  "ĐÚNG. PPF là tập hợp các mức sản lượng tối đa có thể sản xuất với nguồn lực và công nghệ hiện có; điểm bên ngoài vượt quá khả năng đó. Chỉ khi PPF dịch ra ngoài (tăng trưởng) thì điểm đó mới có thể đạt được.", 13)

T(C1, "Kinh tế học vi mô và kinh tế học vĩ mô hoàn toàn độc lập, không liên quan đến nhau.", False,
  "SAI. Vi mô nghiên cứu các đơn vị cá biệt, vĩ mô nghiên cứu nền kinh tế như tổng thể; nhưng các biến động vĩ mô là kết quả của vô số quyết định vi mô nên hai lĩnh vực gắn bó chặt chẽ với nhau.", 17)

T(C1, "\"Năm 2023 tỷ lệ thất nghiệp của Việt Nam khoảng 2,3%\" là một phát biểu thực chứng.", True,
  "ĐÚNG. Phát biểu thực chứng mô tả thế giới như nó vốn có và có thể kiểm chứng bằng số liệu. Câu này không đưa ra đánh giá \"nên\" hay \"không nên\" nên không phải chuẩn tắc.", 18)

T(C1, "Quy luật cầu phát biểu rằng, các yếu tố khác không đổi, khi giá một hàng hóa tăng thì lượng cầu hàng hóa đó tăng.", False,
  "SAI. Quy luật cầu: các yếu tố khác không đổi, khi giá tăng thì lượng cầu GIẢM (quan hệ nghịch biến). Quan hệ đồng biến giữa giá và lượng là quy luật cung.", 21)

T(C1, "Cầu thị trường là tổng cầu của tất cả người mua về một hàng hóa.", True,
  "ĐÚNG. Cầu thị trường được tính bằng cách cộng lượng cầu của tất cả người mua tại mỗi mức giá; tương tự cung thị trường là tổng cung của tất cả người bán.", 27)

# ───────────────────────── CHƯƠNG 2 ─────────────────────────
M(C2, "GDP là giá trị thị trường của:",
  ["Tất cả hàng hóa và dịch vụ cuối cùng được sản xuất trong phạm vi lãnh thổ một nước trong một thời kỳ nhất định",
   "Tất cả hàng hóa trung gian và cuối cùng được sản xuất trong một nước",
   "Tất cả hàng hóa và dịch vụ do công dân một nước sản xuất ra, dù ở đâu",
   "Tất cả hàng hóa được bán ra trong năm, kể cả hàng đã qua sử dụng"],
  "Định nghĩa GDP: giá trị thị trường – hàng hóa và dịch vụ CUỐI CÙNG – sản xuất trong LÃNH THỔ – trong một thời kỳ. "
  "Tính cả hàng trung gian là tính trùng; \"do công dân sản xuất dù ở đâu\" là GNP; hàng đã qua sử dụng không phải sản xuất trong kỳ.", 6)

M(C2, "Vì sao đối với tổng thể nền kinh tế, thu nhập bằng chi tiêu?",
  ["Vì mỗi đồng chi tiêu của người mua là một đồng thu nhập của người bán",
   "Vì chính phủ quy định như vậy",
   "Vì hộ gia đình luôn tiêu hết thu nhập",
   "Vì doanh nghiệp không có lợi nhuận"],
  "Mọi giao dịch đều có người mua và người bán; số tiền người mua chi ra đúng bằng số tiền người bán nhận được. Vì vậy GDP vừa đo tổng thu nhập vừa đo tổng chi tiêu.", 3)

M(C2, "Khoản nào sau đây được tính vào GDP của Việt Nam năm nay?",
  ["Dịch vụ cắt tóc tại một tiệm ở Hà Nội trong năm nay",
   "Bột mì một tiệm bánh mua để làm bánh mì",
   "Một căn nhà xây năm 2010 được bán lại năm nay",
   "Công việc nội trợ một người tự làm tại nhà"],
  "Dịch vụ cắt tóc là hàng vô hình cuối cùng, sản xuất trong kỳ và có giá thị trường → tính vào GDP. "
  "Bột mì là hàng trung gian (đã nằm trong giá bánh mì); nhà xây 2010 thuộc kỳ khác; nội trợ tự làm không qua thị trường nên không tính.", 8)

M(C2, "Vì sao GDP chỉ tính hàng hóa cuối cùng mà không tính hàng hóa trung gian?",
  ["Vì giá trị hàng hóa cuối cùng đã bao gồm giá trị hàng hóa trung gian, tính thêm sẽ bị tính trùng",
   "Vì hàng hóa trung gian không có giá thị trường",
   "Vì hàng hóa trung gian luôn được nhập khẩu",
   "Vì hàng hóa trung gian không do doanh nghiệp sản xuất"],
  "Hàng trung gian được dùng làm đầu vào và đã kết tinh trong giá trị sản phẩm cuối cùng. Nếu cộng cả hai sẽ đếm một giá trị hai lần. Hàng trung gian vẫn có giá thị trường và có thể sản xuất trong nước.", 9)

M(C2, "Một công ty Hàn Quốc sản xuất điện thoại tại nhà máy ở Bắc Ninh. Giá trị điện thoại này được tính vào:",
  ["GDP của Việt Nam",
   "GDP của Hàn Quốc",
   "GNP của Việt Nam",
   "Không tính vào chỉ tiêu nào"],
  "GDP tính theo LÃNH THỔ: sản xuất trong lãnh thổ Việt Nam thì tính vào GDP Việt Nam, dù chủ sở hữu là người nước ngoài. Giá trị này tính vào GNP của Hàn Quốc (theo quốc tịch), không phải GNP Việt Nam.", 11)

M(C2, "Thời kỳ thông thường để tính GDP là:",
  ["Một năm hoặc một quý",
   "Một tuần",
   "Mười năm",
   "Một nhiệm kỳ chính phủ"],
  "Theo bài, GDP thường được tính theo năm hoặc theo quý (3 tháng).", 12)

M(C2, "Công thức tính GDP theo phương pháp chi tiêu là:",
  ["Y = C + I + G + NX",
   "Y = C + I + G + EX + IM",
   "Y = C + S + T",
   "Y = C + I − G + NX"],
  "GDP gồm 4 thành phần chi tiêu: tiêu dùng (C), đầu tư (I), mua sắm của chính phủ (G), xuất khẩu ròng (NX = EX − IM). Cộng cả IM là sai vì nhập khẩu phải trừ đi; C + S + T là cách phân bổ thu nhập.", 13)

M(C2, "Một gia đình sống trong căn nhà của chính mình. Theo cách tính GDP, khoản nào được tính vào tiêu dùng (C)?",
  ["Giá trị \"tiền thuê nhà\" quy đổi mà chủ nhà \"tự trả\" cho chính mình",
   "Giá mua căn nhà",
   "Không tính gì vì không có giao dịch",
   "Tiền lãi vay mua nhà"],
  "Bài nêu: với chủ nhà, C bao gồm \"tiền thuê nhà\" mà người sở hữu tự trả cho mình (giá trị quy đổi). Mua nhà mới thuộc đầu tư (I) vào nhà ở, không phải C.", 14)

M(C2, "Khoản nào sau đây được tính vào ĐẦU TƯ (I) trong GDP?",
  ["Doanh nghiệp mua máy móc mới và hàng tồn kho tăng thêm",
   "Một người mua cổ phiếu của công ty niêm yết",
   "Hộ gia đình mua tủ lạnh",
   "Chính phủ trả trợ cấp thất nghiệp"],
  "I gồm đầu tư cố định vào kinh doanh, đầu tư cố định vào nhà ở và đầu tư vào hàng tồn kho. Mua cổ phiếu là giao dịch tài chính (chuyển quyền sở hữu), không tạo hàng hóa mới; tủ lạnh thuộc C; trợ cấp là chi chuyển khoản.", 15)

M(C2, "Khoản nào KHÔNG được tính vào mua sắm của chính phủ (G)?",
  ["Trợ cấp cho người già",
   "Lương trả cho giáo viên trường công",
   "Chi xây dựng đường cao tốc",
   "Mua trang thiết bị quân sự"],
  "G là chi tiêu của chính phủ cho hàng hóa, dịch vụ. Trợ cấp người già, trợ cấp thất nghiệp là chi CHUYỂN KHOẢN — chỉ chuyển thu nhập, không đổi lại hàng hóa/dịch vụ nào nên không tính vào G.", 16)

M(C2, "Xuất khẩu ròng (NX) được tính bằng:",
  ["Xuất khẩu − Nhập khẩu",
   "Xuất khẩu + Nhập khẩu",
   "Nhập khẩu − Xuất khẩu",
   "Xuất khẩu − Tiêu dùng"],
  "NX = EX − IM. Xuất khẩu là chi tiêu của nước ngoài cho hàng trong nước (cộng vào), nhập khẩu là phần C, I, G chi cho hàng sản xuất ở nước ngoài (phải trừ ra).", 17)

M(C2, "Một hộ gia đình Việt Nam mua chiếc ô tô 1 tỷ đồng nhập khẩu nguyên chiếc từ Nhật. Tác động đến GDP Việt Nam là:",
  ["C tăng 1 tỷ, NX giảm 1 tỷ, GDP không đổi",
   "C tăng 1 tỷ, GDP tăng 1 tỷ",
   "NX tăng 1 tỷ, GDP tăng 1 tỷ",
   "I tăng 1 tỷ, GDP tăng 1 tỷ"],
  "Chi mua xe tính vào C nhưng xe sản xuất ở nước ngoài nên nhập khẩu tăng 1 tỷ (NX giảm 1 tỷ). Hai tác động triệt tiêu, GDP không đổi — đúng vì xe không được sản xuất trong lãnh thổ Việt Nam.", 17)

M(C2, "GDP danh nghĩa khác GDP thực tế ở điểm nào?",
  ["GDP danh nghĩa tính theo giá hiện hành, GDP thực tế tính theo giá năm cơ sở",
   "GDP danh nghĩa tính theo giá năm cơ sở, GDP thực tế tính theo giá hiện hành",
   "GDP danh nghĩa chỉ tính hàng hóa, GDP thực tế tính cả dịch vụ",
   "GDP danh nghĩa không tính xuất khẩu ròng"],
  "GDP danh nghĩa dùng giá hiện hành, chưa điều chỉnh lạm phát; GDP thực tế dùng giá năm cơ sở nên đã loại bỏ ảnh hưởng của lạm phát. Cả hai đều tính đầy đủ hàng hóa, dịch vụ và NX.", 18)

M(C2, "Ví dụ trong bài: năm 2003 sản xuất 500 đơn vị hàng X (giá $11) và 1100 đơn vị hàng Y (giá $2,50). GDP danh nghĩa năm 2003 là:",
  ["$8.250",
   "$7.200",
   "$6.000",
   "$10.800"],
  "GDP danh nghĩa 2003 = 11×500 + 2,5×1100 = 5.500 + 2.750 = $8.250 (dùng giá hiện hành của năm 2003). $7.200 là GDP thực tế 2003 theo giá 2002; $6.000 là GDP năm 2002; $10.800 là GDP danh nghĩa 2004.", 19)

M(C2, "Với năm cơ sở 2002 (giá X = $10, giá Y = $2), năm 2004 sản xuất 600 X và 1200 Y. GDP thực tế năm 2004 là:",
  ["$8.400",
   "$10.800",
   "$7.200",
   "$9.600"],
  "GDP thực tế 2004 = 10×600 + 2×1200 = 6.000 + 2.400 = $8.400 (lượng năm 2004 × giá năm cơ sở 2002). $10.800 là GDP danh nghĩa 2004 (dùng giá 2004).", 20)

M(C2, "Chỉ số giảm phát GDP được tính bằng công thức:",
  ["100 × GDP danh nghĩa / GDP thực tế",
   "100 × GDP thực tế / GDP danh nghĩa",
   "GDP danh nghĩa − GDP thực tế",
   "100 × CPI năm nay / CPI năm trước"],
  "Chỉ số giảm phát GDP = (GDP danh nghĩa / GDP thực tế) × 100; nó đo mức giá chung của hàng hóa sản xuất trong nước. Năm cơ sở chỉ số bằng 100.", 22)

M(C2, "GDP danh nghĩa năm 2003 là $8.250, GDP thực tế là $7.200. Chỉ số giảm phát GDP năm 2003 xấp xỉ:",
  ["114,6",
   "87,3",
   "100,0",
   "128,6"],
  "Chỉ số giảm phát = 100 × 8.250/7.200 ≈ 114,6. 87,3 là do đảo ngược tử/mẫu; 100 là năm cơ sở 2002; 128,6 là chỉ số năm 2004.", 23)

M(C2, "Chỉ số giảm phát GDP năm 2003 là 114,6 và năm 2004 là 128,6. Tỷ lệ lạm phát năm 2004 tính theo chỉ số này xấp xỉ:",
  ["12,2%",
   "14,0%",
   "28,6%",
   "14,6%"],
  "Lạm phát = (128,6 − 114,6)/114,6 × 100% ≈ 12,2%. 14,0 chỉ là chênh lệch điểm (chưa chia cho năm trước); 28,6% là so với năm cơ sở; 14,6% là lạm phát năm 2003.", 23)

M(C2, "Hạn chế nào sau đây là lý do GDP KHÔNG phải thước đo hoàn hảo cho phúc lợi xã hội?",
  ["GDP không tính đến thời gian nghỉ ngơi và các giao dịch phi thị trường",
   "GDP có tính đến chất lượng môi trường",
   "GDP tính cả giá trị hàng hóa trung gian",
   "GDP đo lường cả chất lượng sản phẩm"],
  "Bài nêu GDP là chỉ số đo về lượng; không tính dân số, thời gian nghỉ ngơi, chất lượng sản phẩm, tác động ngoại vi (như môi trường) và giao dịch phi thị trường. Các phương án còn lại mô tả sai GDP.", 24)

M(C2, "Tổng sản phẩm quốc dân (GNP) được tính bằng:",
  ["GNP = GDP + thu nhập nhân tố ròng từ nước ngoài (NIA)",
   "GNP = GDP − xuất khẩu ròng",
   "GNP = GDP + nhập khẩu",
   "GNP = GDP − khấu hao"],
  "GNP đo giá trị hàng hóa, dịch vụ cuối cùng do CÔNG DÂN một nước sản xuất: GNP = GDP + NIA, với NIA = thu nhập yếu tố công dân nhận từ nước ngoài − thu nhập yếu tố người nước ngoài nhận từ trong nước.", 25)

M(C2, "Chỉ số giá tiêu dùng (CPI) là:",
  ["Thước đo chi phí tổng quát của hàng hóa và dịch vụ được mua bởi một người tiêu dùng điển hình",
   "Thước đo giá của tất cả hàng hóa và dịch vụ sản xuất trong nước",
   "Tỷ lệ phần trăm thay đổi GDP thực tế",
   "Giá trị hàng hóa mà doanh nghiệp bán ra"],
  "Định nghĩa CPI trong bài. \"Giá của tất cả hàng hóa, dịch vụ sản xuất trong nước\" là chỉ số giảm phát GDP; % thay đổi GDP thực tế là tốc độ tăng trưởng.", 27)

M(C2, "Bước ĐẦU TIÊN trong phương pháp tính CPI là:",
  ["Cố định giỏ hàng hóa thông qua khảo sát hành vi mua của người tiêu dùng",
   "Xác định giá từng mặt hàng tại mỗi thời điểm",
   "Tính chi phí của giỏ hàng",
   "Chọn năm cơ sở và tính chỉ số"],
  "4 bước tính CPI: (1) cố định giỏ hàng, (2) xác định giá, (3) tính chi phí giỏ hàng, (4) chọn năm cơ sở và tính chỉ số. Phải biết giỏ hàng gồm gì trước thì mới thu thập giá được.", 28)

M(C2, "CPI năm 2007 = 100, năm 2008 = 158, năm 2009 = 217. Tỷ lệ lạm phát năm 2009 xấp xỉ:",
  ["37%",
   "59%",
   "117%",
   "58%"],
  "Lạm phát 2009 = (217 − 158)/158 × 100% ≈ 37,3%. 59 chỉ là chênh lệch điểm; 117% là so với năm 2007 (năm cơ sở); 58% là lạm phát năm 2008.", 29)

M(C2, "Lãi suất danh nghĩa là 8%/năm, tỷ lệ lạm phát là 5%/năm. Lãi suất thực xấp xỉ:",
  ["3%",
   "13%",
   "1,6%",
   "−3%"],
  "Lãi suất thực = lãi suất danh nghĩa − tỷ lệ lạm phát = 8% − 5% = 3%. Đây là mức tăng sức mua thực tế của khoản tiền gửi.", 35)

T(C2, "GDP vừa đo lường tổng thu nhập vừa đo lường tổng chi tiêu của nền kinh tế.", True,
  "ĐÚNG. Với toàn bộ nền kinh tế, mỗi đồng chi tiêu của người mua là một đồng thu nhập của người bán, nên tổng thu nhập luôn bằng tổng chi tiêu và cả hai bằng GDP.", 3)

T(C2, "GDP tính cả giá trị các hàng hóa được buôn bán bất hợp pháp như ma túy.", False,
  "SAI. GDP chỉ bao gồm hàng hóa được sản xuất và bán HỢP PHÁP trên thị trường. Hàng hóa bất hợp pháp không được ghi nhận (và cũng khó đo lường).", 7)

T(C2, "GDP bao gồm cả hàng hóa hữu hình và dịch vụ vô hình.", True,
  "ĐÚNG. GDP gồm hàng hóa hữu hình (thức ăn, quần áo, xe máy) và hàng hóa vô hình (cắt tóc, vệ sinh nhà cửa, buổi hòa nhạc).", 8)

T(C2, "Lốp xe mà nhà máy ô tô mua về để lắp vào xe mới được tính riêng vào GDP bên cạnh giá trị chiếc xe.", False,
  "SAI. Lốp xe trong trường hợp này là hàng trung gian; giá trị của nó đã nằm trong giá chiếc xe (hàng cuối cùng). Tính riêng sẽ bị tính trùng.", 9)

T(C2, "Việc bán lại một chiếc xe máy đã qua sử dụng (sản xuất từ năm trước) làm tăng GDP năm nay đúng bằng giá bán của xe.", False,
  "SAI. GDP chỉ tính hàng hóa sản xuất trong thời kỳ đang xét. Chiếc xe đã được tính vào GDP năm nó được sản xuất; giao dịch bán lại chỉ chuyển quyền sở hữu. (Chỉ phí dịch vụ môi giới, nếu có, mới được tính.)", 10)

T(C2, "Thu nhập của một kỹ sư người Việt làm việc tại Nhật được tính vào GDP của Việt Nam.", False,
  "SAI. GDP tính theo lãnh thổ: thu nhập này tạo ra trong lãnh thổ Nhật nên tính vào GDP Nhật. Nó được tính vào GNP của Việt Nam (thông qua thu nhập nhân tố ròng từ nước ngoài).", 11)

T(C2, "Chi tiêu của hộ gia đình (C) bao gồm chi cho hàng hóa lâu bền, hàng hóa không lâu bền và dịch vụ.", True,
  "ĐÚNG. Theo bài, C là tổng chi tiêu của hộ gia đình cho hàng hóa (lâu bền và không lâu bền) và dịch vụ. Riêng mua nhà mới được tính vào đầu tư.", 14)

T(C2, "Phần hàng hóa sản xuất ra trong năm nhưng chưa bán được, được đưa vào kho, vẫn được tính vào GDP năm đó.", True,
  "ĐÚNG. Phần tăng hàng tồn kho được tính vào đầu tư (I) — doanh nghiệp được xem như \"tự mua\" hàng của mình. Nhờ vậy GDP phản ánh đúng lượng sản xuất trong kỳ.", 15)

T(C2, "Trợ cấp thất nghiệp được tính vào mua sắm của chính phủ (G).", False,
  "SAI. Trợ cấp thất nghiệp là chi chuyển khoản: chính phủ chuyển thu nhập cho người dân mà không nhận lại hàng hóa hay dịch vụ nào, nên không tính vào G (và không tính vào GDP).", 16)

T(C2, "Thay đổi trong GDP thực tế chỉ phản ánh sự thay đổi về số lượng hàng hóa, dịch vụ được sản xuất.", True,
  "ĐÚNG. GDP thực tế cố định giá ở năm cơ sở, nên khi nó thay đổi thì chỉ có thể do lượng sản xuất thay đổi. GDP danh nghĩa thì phản ánh cả thay đổi giá lẫn lượng.", 21)

T(C2, "Tại năm cơ sở, GDP danh nghĩa bằng GDP thực tế nên chỉ số giảm phát GDP bằng 100.", True,
  "ĐÚNG. Ở năm cơ sở, giá hiện hành chính là giá năm cơ sở nên GDP danh nghĩa = GDP thực tế, và chỉ số giảm phát = 100 × 1 = 100 (ví dụ năm 2002 trong bài).", 23)

T(C2, "GDP là chỉ tiêu phản ánh cả số lượng lẫn chất lượng của hàng hóa và dịch vụ trong nền kinh tế.", False,
  "SAI. Bài nhấn mạnh GDP là chỉ số đo về LƯỢNG, không phải chất; nó không phản ánh chất lượng sản phẩm, thời gian nghỉ ngơi, tác động ngoại vi hay giao dịch phi thị trường.", 24)

T(C2, "Với nước có nhiều lao động làm việc ở nước ngoài gửi thu nhập về (NIA > 0), GNP lớn hơn GDP.", True,
  "ĐÚNG. GNP = GDP + NIA. Khi thu nhập nhân tố công dân nhận từ nước ngoài lớn hơn phần người nước ngoài nhận từ trong nước (NIA > 0) thì GNP > GDP.", 25)

T(C2, "CPI phản ánh giá của cả hàng hóa nhập khẩu mà người tiêu dùng mua, còn chỉ số giảm phát GDP chỉ phản ánh giá hàng sản xuất trong nước.", True,
  "ĐÚNG. CPI đo giá giỏ hàng người tiêu dùng mua (gồm hàng nội địa và ngoại nhập); chỉ số giảm phát GDP đo giá mọi hàng hóa, dịch vụ sản xuất trong nước.", 31)

T(C2, "CPI sử dụng giỏ hàng có quyền số thay đổi mỗi năm, còn chỉ số giảm phát GDP dùng giỏ hàng cố định.", False,
  "SAI. Ngược lại: CPI dùng giỏ hàng CỐ ĐỊNH (quyền số không đổi), còn chỉ số giảm phát GDP có quyền số thay đổi theo cơ cấu sản xuất từng năm.", 31)

T(C2, "\"Thiên vị thay thế\" là một trong các vấn đề khiến CPI đo lường chi phí sinh hoạt chưa chính xác.", True,
  "ĐÚNG. Khi giá một mặt hàng tăng, người tiêu dùng chuyển sang mặt hàng rẻ hơn, nhưng CPI vẫn giữ giỏ hàng cố định nên phóng đại mức tăng chi phí sinh hoạt. Hai vấn đề khác là hàng hóa mới và thay đổi chất lượng không đo lường được.", 30)

# ───────────────────────── CHƯƠNG 3 ─────────────────────────
M(C3, "Tăng trưởng kinh tế là:",
  ["Sự gia tăng quy mô sản lượng của nền kinh tế trong một thời kỳ nhất định",
   "Sự gia tăng mức giá chung của nền kinh tế",
   "Sự gia tăng dân số của một quốc gia",
   "Sự gia tăng lượng tiền trong lưu thông"],
  "Định nghĩa trong bài. Gia tăng mức giá chung là lạm phát; dân số hay lượng tiền tăng không đồng nghĩa với sản lượng tăng.", 5)

M(C3, "GDP thực tế năm 2023 là 500 tỷ, năm 2024 là 530 tỷ. Tốc độ tăng trưởng kinh tế năm 2024 là:",
  ["6%",
   "30%",
   "5,7%",
   "106%"],
  "g = (GDPt − GDPt−1)/GDPt−1 × 100% = (530 − 500)/500 × 100% = 6%. 5,7% là do chia nhầm cho 530; 30 chỉ là mức tăng tuyệt đối (tỷ); 106% là tỷ số GDPt/GDPt−1.", 5)

M(C3, "Theo bài, điều nào sau đây đúng về thứ hạng thu nhập giữa các nước theo thời gian?",
  ["Thứ hạng có thể thay đổi vì tốc độ tăng trưởng giữa các nước khác nhau",
   "Nước nghèo luôn mãi là nước nghèo",
   "Nước giàu luôn giữ vững vị trí của mình",
   "Thứ hạng chỉ thay đổi khi có chiến tranh"],
  "Do tốc độ tăng trưởng khác nhau, nước nghèo không nhất thiết mãi nghèo, và nước giàu cũng không được đảm bảo vị trí — có thể bị nước nghèo hơn nhưng tăng trưởng nhanh hơn vượt qua.", 8)

M(C3, "Kiến thức, kỹ năng mà người lao động có được thông qua giáo dục, đào tạo và kinh nghiệm được gọi là:",
  ["Vốn nhân lực (H)",
   "Vốn vật chất (K)",
   "Tài nguyên thiên nhiên (N)",
   "Kiến thức công nghệ (A)"],
  "Đó là định nghĩa vốn nhân lực (H). Vốn vật chất là máy móc, cơ sở hạ tầng; tài nguyên thiên nhiên do tự nhiên cung cấp; công nghệ là hiểu biết của XÃ HỘI về cách sản xuất tốt nhất (còn H gắn với từng người lao động).", 19)

M(C3, "Trữ lượng máy móc, thiết bị và cơ sở hạ tầng dùng để sản xuất hàng hóa và dịch vụ được gọi là:",
  ["Vốn vật chất (tư bản) K",
   "Vốn nhân lực H",
   "Tài nguyên thiên nhiên N",
   "Tiến bộ công nghệ A"],
  "Vốn vật chất (K) là trữ lượng máy móc, thiết bị và cấu trúc cơ sở hạ tầng — bản thân chúng cũng là sản phẩm được sản xuất ra để dùng cho sản xuất.", 18)

M(C3, "Trong hàm sản xuất Y = A·F(L, K, H, N), biến A thể hiện:",
  ["Trình độ công nghệ",
   "Lượng lao động",
   "Tài nguyên thiên nhiên",
   "Vốn nhân lực"],
  "A là kiến thức công nghệ — nhân với F(·) nên khi A tăng, cùng lượng đầu vào sẽ cho nhiều sản lượng hơn. L là lao động, N là tài nguyên thiên nhiên, H là vốn nhân lực.", 14)

M(C3, "Hàm sản xuất nào sau đây có lợi suất KHÔNG ĐỔI theo quy mô?",
  ["Y = L^(1/2) · K^(1/2)",
   "Y = 2KL",
   "Y = K² + L",
   "Y = K·L²"],
  "Nhân L và K với z: (zL)^½(zK)^½ = z·L^½K^½ = zY → lợi suất không đổi. Với Y = 2KL: 2(zK)(zL) = z²Y → sản lượng tăng nhanh hơn (lợi suất tăng). Hai hàm còn lại cũng không cho đúng zY.", 15)

M(C3, "Năng suất được định nghĩa là:",
  ["Số lượng hàng hóa và dịch vụ được sản xuất ra từ mỗi đơn vị nhập lượng lao động",
   "Tổng sản lượng của nền kinh tế",
   "Số giờ làm việc của mỗi lao động",
   "Tổng số vốn đầu tư trong năm"],
  "Năng suất = Y/L — sản lượng trên mỗi đơn vị lao động. Tổng sản lượng (Y) chưa chia cho lao động nên không phản ánh năng suất.", 16)

M(C3, "Với hàm sản xuất có lợi suất không đổi theo quy mô, chọn z = 1/L ta được Y/L = A·F(1, K/L, H/L, N/L). Năng suất KHÔNG phụ thuộc trực tiếp vào yếu tố nào sau đây?",
  ["Mức giá chung của nền kinh tế",
   "Tư bản trên mỗi lao động (K/L)",
   "Vốn nhân lực trên mỗi lao động (H/L)",
   "Trình độ công nghệ (A)"],
  "Theo công thức, năng suất Y/L phụ thuộc vào A, K/L, H/L và N/L. Mức giá chung không có trong hàm sản xuất — hàm sản xuất mô tả quan hệ giữa các lượng đầu vào và đầu ra thực.", 17)

M(C3, "Vì sao một số nước như Nhật Bản vẫn giàu dù ít tài nguyên thiên nhiên?",
  ["Họ có thể nhập khẩu tài nguyên và dựa vào vốn vật chất, vốn nhân lực, công nghệ",
   "Vì tài nguyên thiên nhiên không ảnh hưởng gì đến sản lượng",
   "Vì Nhật Bản in nhiều tiền",
   "Vì Nhật Bản có dân số tăng rất nhanh"],
  "Bài nêu: một số nước không cần nhiều N để giàu có (Nhật nhập khẩu N cần thiết). Tài nguyên vẫn có ảnh hưởng (N/L tăng → Y/L tăng) nhưng không phải điều kiện bắt buộc. In tiền gây lạm phát; dân số tăng nhanh làm giảm GDP bình quân.", 20)

M(C3, "Theo bài, yếu tố nào được xem là \"trung chuyển\" tri thức công nghệ vào quá trình sản xuất dùng tư bản hiện vật?",
  ["Vốn nhân lực",
   "Tài nguyên thiên nhiên",
   "Lao động giản đơn",
   "Đầu tư gián tiếp nước ngoài"],
  "Bài nêu: vốn nhân lực là yếu tố trung chuyển tri thức công nghệ vào quá trình sản xuất dùng tư bản hiện vật — người có kiến thức, kỹ năng mới vận dụng được công nghệ vào máy móc.", 21)

M(C3, "Quy luật sinh lợi (lợi suất) giảm dần của tư bản nói rằng:",
  ["Khi K tăng, sản lượng tăng thêm từ mỗi đơn vị tư bản bổ sung sẽ giảm xuống",
   "Khi K tăng, tổng sản lượng giảm xuống",
   "Khi K tăng, sản lượng tăng thêm từ mỗi đơn vị tư bản bổ sung sẽ tăng lên",
   "Khi lao động tăng, tư bản giảm"],
  "Sinh lợi giảm dần: tổng sản lượng vẫn TĂNG khi K tăng, nhưng phần tăng thêm do mỗi đơn vị K bổ sung ngày càng NHỎ. Nhầm \"tổng sản lượng giảm\" là lỗi thường gặp.", 26)

M(C3, "\"Hiệu ứng đuổi kịp\" là đặc tính theo đó:",
  ["Các nước khởi đầu nghèo có xu hướng tăng trưởng nhanh hơn các nước khởi đầu giàu",
   "Các nước giàu luôn tăng trưởng nhanh hơn các nước nghèo",
   "Mọi nước đều có cùng tốc độ tăng trưởng",
   "Các nước nghèo không thể bắt kịp các nước giàu"],
  "Do sinh lợi giảm dần, nước nghèo có ít K/L nên thêm một đơn vị tư bản làm năng suất tăng nhiều; nước giàu đã có nhiều K/L nên tăng thêm ít. Vì vậy nước nghèo có xu hướng tăng trưởng nhanh hơn.", 28)

M(C3, "Nhà đầu tư nước ngoài bỏ vốn xây nhà máy tại Việt Nam và trực tiếp tham gia quản lý doanh nghiệp. Đây là hình thức:",
  ["Đầu tư trực tiếp nước ngoài",
   "Đầu tư gián tiếp nước ngoài",
   "Viện trợ không hoàn lại",
   "Xuất khẩu ròng"],
  "Đầu tư trực tiếp (FDI): người nước ngoài mang vốn vào và trực tiếp quản lý doanh nghiệp. Đầu tư gián tiếp: mang vốn vào (ví dụ mua cổ phiếu) nhưng không tham gia quản lý.", 29)

M(C3, "Một quỹ nước ngoài mua 3% cổ phiếu của một công ty niêm yết Việt Nam nhưng không tham gia điều hành. Đây là:",
  ["Đầu tư gián tiếp nước ngoài",
   "Đầu tư trực tiếp nước ngoài",
   "Đầu tư vào hàng tồn kho",
   "Mua sắm của chính phủ"],
  "Mang vốn vào đầu tư nhưng KHÔNG tham gia quản lý doanh nghiệp (mua cổ phiếu…) là đầu tư gián tiếp nước ngoài.", 29)

M(C3, "Hiện tượng \"chảy máu chất xám\" gây ảnh hưởng trực tiếp đến nguồn lực tăng trưởng nào?",
  ["Vốn nhân lực (H)",
   "Tài nguyên thiên nhiên (N)",
   "Vốn vật chất (K)",
   "Đất đai"],
  "Chảy máu chất xám là việc lao động có trình độ cao ra nước ngoài làm việc, làm giảm vốn nhân lực trong nước — vấn đề bài nêu trong phần đầu tư giáo dục và đào tạo.", 30)

M(C3, "Tốc độ gia tăng dân số cao có thể gây tác động nào sau đây?",
  ["Làm giảm GDP bình quân đầu người và tạo gánh nặng cho hệ thống giáo dục",
   "Luôn làm tăng GDP bình quân đầu người",
   "Làm tăng tư bản trên mỗi lao động",
   "Không ảnh hưởng đến mức sống"],
  "Bài nêu: tốc độ tăng dân số cao làm giảm GDP bình quân đầu người và tạo gánh nặng cho giáo dục; dân số tăng nhanh cũng làm K/L bị \"pha loãng\". Vì vậy kiểm soát gia tăng dân số giúp nước kém phát triển cải thiện mức sống.", 33)

M(C3, "Biện pháp nào sau đây là cách chính phủ khuyến khích nghiên cứu và phát triển (R&D)?",
  ["Hệ thống công nhận và bảo hộ sáng chế",
   "Tăng thuế đối với sản xuất dùng công nghệ mới",
   "Hạn chế nhập khẩu tri thức nước ngoài",
   "Cắt giảm ngân sách giáo dục"],
  "Bài liệt kê: các chương trình tài trợ, hỗ trợ nghiên cứu; GIẢM thuế cho sản xuất dùng công nghệ mới; hệ thống công nhận và bảo hộ sáng chế. Các phương án khác đi ngược lại mục tiêu khuyến khích R&D.", 34)

T(C3, "Tốc độ tăng trưởng kinh tế hàng năm được tính bằng (GDPt − GDPt−1)/GDPt−1 × 100%.", True,
  "ĐÚNG. Đây là công thức tốc độ tăng trưởng mỗi năm trong bài: phần trăm thay đổi GDP (thực tế) năm t so với năm t−1.", 5)

T(C3, "Mức sống của một quốc gia phụ thuộc vào khả năng sản xuất hàng hóa và dịch vụ, và khả năng này phụ thuộc vào năng suất.", True,
  "ĐÚNG. Bài khẳng định: mức sống phụ thuộc khả năng sản xuất, mà khả năng sản xuất phụ thuộc vào năng suất (nối với nguyên lý 8 ở Chương 1).", 14)

T(C3, "Hàm sản xuất Y = 2KL có lợi suất không đổi theo quy mô.", False,
  "SAI. Khi nhân K và L với z: 2(zK)(zL) = z²·2KL = z²Y. Sản lượng tăng theo z² (nhiều hơn z lần) nên đây là lợi suất TĂNG theo quy mô. Hàm Y = L^½K^½ mới có lợi suất không đổi.", 15)

T(C3, "Khi năng suất lao động tăng nhanh thì mức sống của người dân cũng tăng nhanh.", True,
  "ĐÚNG. Theo bài, năng suất cao → GDP thực tế và thu nhập cao; năng suất tăng nhanh thì mức sống cũng tăng nhanh.", 16)

T(C3, "Tăng tư bản trên mỗi lao động (K/L) dẫn đến tăng năng suất (Y/L).", True,
  "ĐÚNG. Công nhân có nhiều công cụ làm việc (máy móc, thiết bị) hơn sẽ đạt năng suất cao hơn: tăng K/L dẫn đến tăng Y/L.", 18)

T(C3, "Quốc gia muốn giàu có bắt buộc phải có nguồn tài nguyên thiên nhiên dồi dào.", False,
  "SAI. Tài nguyên giúp tăng năng suất (như Ả Rập Saudi có dầu mỏ), nhưng không phải điều kiện bắt buộc: Nhật Bản ít tài nguyên vẫn giàu nhờ nhập khẩu tài nguyên và dựa vào K, H, công nghệ.", 20)

T(C3, "Tiến bộ công nghệ cho phép xã hội có thêm nhiều sản lượng hơn từ cùng một lượng nguồn lực.", True,
  "ĐÚNG. Tiến bộ công nghệ là kiến thức tiên tiến giúp đẩy mạnh năng suất — cùng nguồn lực nhưng sản xuất được nhiều hơn.", 21)

T(C3, "Khi xã hội đầu tư nhiều hơn cho tư bản thì phải giảm tiêu dùng hiện tại và tiết kiệm nhiều hơn.", True,
  "ĐÚNG. Nguồn lực có hạn: muốn dành nhiều nguồn lực cho sản xuất hàng tư bản thì phải tiêu dùng ít lại, tiết kiệm nhiều hơn — đánh đổi giữa hiện tại và tương lai.", 24)

T(C3, "Nhờ tăng tiết kiệm và đầu tư, một quốc gia có thể duy trì tốc độ tăng trưởng cao hơn mãi mãi.", False,
  "SAI. Do quy luật sinh lợi giảm dần, tăng tiết kiệm và đầu tư chỉ giúp tăng trưởng nhanh hơn trong một khoảng thời gian nhất định; khi K đã lớn, mỗi đơn vị K bổ sung tạo thêm ít sản lượng hơn.", 26)

T(C3, "Đầu tư nước ngoài vừa làm tăng trữ lượng tư bản trong nước, vừa có thể giúp nước kém phát triển tiếp thu công nghệ tiên tiến.", True,
  "ĐÚNG. Bài nêu cả hai lợi ích: tăng trữ lượng tư bản và giúp nước kém phát triển thừa kế công nghệ tiên tiến từ các nước phát triển hơn.", 29)

T(C3, "Bảo vệ quyền sở hữu tài sản và ổn định chính trị không ảnh hưởng đến tăng trưởng kinh tế.", False,
  "SAI. Bài khẳng định chính phủ có thể thúc đẩy tăng trưởng qua bảo vệ quyền sở hữu và ổn định chính trị; nước có tòa án hiệu quả, công chức trung thực, chính trị ổn định sẽ có mức sống cao hơn.", 31)

T(C3, "Theo bài, các nước nghèo sẽ có lợi khi áp dụng chính sách hướng ngoại, dỡ bỏ rào cản thương mại.", True,
  "ĐÚNG. Chính sách hướng ngoại giúp hội nhập kinh tế thế giới; dỡ bỏ rào cản thương mại có tác dụng tăng trưởng giống như có tiến bộ công nghệ.", 32)


def build():
    rng = random.Random(20261010)
    out = []
    for i, item in enumerate(BANK, 1):
        kind, ch, question, payload, why, slide = item
        note = f"{SRC[ch]}, slide {slide}"
        if kind == "mcq":
            correct = payload[0]
            opts = payload[:]
            rng.shuffle(opts)
            letters = "ABCD"
            options = {letters[k]: o for k, o in enumerate(opts)}
            ans = letters[opts.index(correct)]
            explanation = f"Đáp án đúng: {ans}. {correct}\n\n{why}"
        else:
            options = {"A": "Đúng", "B": "Sai"}
            ans = "A" if payload else "B"
            explanation = why
        out.append({
            "id": i,
            "type": kind,
            "question": question,
            "options": options,
            "answers": [ans],
            "choose": 1,
            "note": note,
            "alt": None,
            "explanation": explanation,
            "exam": ch,
        })
    data = {
        "title": "Kinh tế vĩ mô – Chương 1–3",
        "code": "KTVM",
        "subject": "KTVM",
        "total": len(out),
        "questions": out,
    }
    dst = Path(__file__).resolve().parent.parent / "data" / "ktvm.json"
    dst.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    n_mcq = sum(q["type"] == "mcq" for q in out)
    print(f"{len(out)} câu ({n_mcq} trắc nghiệm, {len(out) - n_mcq} đúng/sai) → {dst}")


if __name__ == "__main__":
    build()
