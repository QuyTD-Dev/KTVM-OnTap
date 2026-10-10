# Ôn tập Kinh tế vĩ mô (Chương 1–3)

Web ôn trắc nghiệm Kinh tế vĩ mô — 100 câu, dựng lại từ web ôn tập HCM202_OnTap.

- **60 câu trắc nghiệm** 4 đáp án và **40 câu Đúng / Sai**, bám theo slide:
  - Chương 1 – Giới thiệu về kinh tế học vĩ mô (10 nguyên lý, sơ đồ chu chuyển, PPF, cung – cầu)
  - Chương 2 – Dữ liệu kinh tế vĩ mô (GDP, GDP thực/danh nghĩa, chỉ số giảm phát, GNP, CPI, lãi suất thực)
  - Chương 3 – Sản xuất và tăng trưởng (năng suất, hàm sản xuất, sinh lợi giảm dần, chính sách tăng trưởng)
- Sau khi trả lời: hiện đáp án đúng, **giải thích vì sao đúng / vì sao sai** và slide nguồn.
- Lọc theo dạng câu, câu sai / chưa làm / đánh dấu ★, chế độ ngẫu nhiên, bản đồ câu, tìm kiếm (Ctrl+K), sáng/tối, đồng bộ tiến độ.

## Chạy trên máy

```bash
python -m http.server 8000
```

Mở `http://localhost:8000`.

## Sửa câu hỏi

Ngân hàng câu hỏi nằm trong `tools/build_questions.py` (`M(...)` = trắc nghiệm, đáp án đúng viết đầu tiên và được xáo vị trí tự động; `T(...)` = Đúng/Sai). Sau khi sửa:

```bash
python tools/build_questions.py
```

để sinh lại `data/ktvm.json`.
