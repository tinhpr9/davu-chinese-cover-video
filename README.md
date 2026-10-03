# Dạ Vũ (夜舞) - Chinese Version Viral TikTok Video

> **Hot Trend TikTok**: Video âm nhạc chuyển ngữ bài hit **"Dạ Vũ" (Tăng Duy Tân x Phong Max)** sang phiên bản tiếng Trung, giọng hát chuẩn phòng thu của nữ ca sĩ **Hoàng Linh (黄龄)**.

---

## 📌 Tổng Quan Dự Án
- **Bài hát**: Dạ Vũ (夜舞 - Yè Wǔ)
- **Tác giả gốc**: Tăng Duy Tân × Phong Max
- **Ca sĩ thể hiện**: Hoàng Linh (黄龄)
- **Định dạng video**: 1080x1920 (Vertical 9:16), 30 FPS, Chuẩn video ngắn TikTok / Reels / Shorts
- **Thời lượng**: 56 giây (đoạn cao trào viral từ 00:32 đến 01:28 với đoạn drop beat sáo trúc và đàn tranh cực cháy)

---

## ✨ Điểm Nổi Bật Thiết Kế
1. **Phụ đề 3 tầng (3-Layer Subtitles) chuẩn xu hướng TikTok**:
   - **Tầng 1 (Hán tự)**: Chữ Hán giản thể to rõ, viền bóng đổ tương phản cao (`Noto Sans CJK SC`, 56pt).
   - **Tầng 2 (Pinyin)**: Phiên âm Hán ngữ đầy đủ dấu thanh điệu, màu vàng kim sang trọng (`DejaVu Sans`, 32pt italic).
   - **Tầng 3 (Việt sub)**: Lời dịch nghĩa tiếng Việt trau chuốt, màu trắng sáng ánh xanh (`DejaVu Sans`, 38pt).
2. **Visual Đậm Chất Á Đông & Hiệu Ứng Sóng Nhạc Động**:
   - Hình nền trăng tròn đêm dạ vũ huyền ảo chuyển động cinematic (Ken Burns Zoompan).
   - Sóng âm thời gian thực (Audio Waveform) phản ứng theo từng nhịp bass và giọng ca sĩ.
   - Nhãn highlight thời khắc vàng bùng nổ Drop Beat.

---

## 📜 Lời Bài Hát & Phiên Âm
| Thời gian | Hán tự | Pinyin | Dịch nghĩa tiếng Việt |
| :--- | :--- | :--- | :--- |
| `03.5s - 10.5s` | **树影灯影底随月影在摇晃** | *Shù yǐng dēng yǐng dǐ suí yuè yǐng zài yáo huàng* | Bóng cây ánh đèn cùng đung đưa theo ánh trăng |
| `10.5s - 18.0s` | **慌的心中所想无处去隐藏** | *Huāng de xīn zhōng suǒ xiǎng wú chù qù yǐn cáng* | Những ý nghĩ hoang mang trong lòng chẳng nơi giấu kín |
| `18.0s - 26.0s` | **勾勒出被遗忘的念念不忘** | *Gōu lè chū bèi yí wàng de niàn niàn bù wàng* | Họa lại những vương vấn tưởng chừng đã lãng quên |
| `26.0s - 34.0s` | **冰凉的是否还能变滚烫** | *Bīng liáng de shì fǒu hái néng biàn gǔn tàng* | Liệu lạnh giá này có thể trở lại nồng say? |
| `34.0s - 42.0s` | **谁翻云覆雨冷不防** | *Shéi fān yún fù yǔ lěng bù fáng* | Ai bất chợt tạo nên phong ba khôn lường... |
| `42.0s - 56.0s` | **随风起舞 叹这长夜** | *Suí fēng qǐ wǔ, tàn zhè cháng yè* | Vũ điệu cùng gió, thở than giữa đêm trường... *(⚡ SIÊU PHẨM DROP BEAT)* |

---

## 🛠 Cấu Trúc Mã Nguồn
```tree
.
├── assets/
│   ├── background_base.jpg          # Artwork nền dọc 1080x1920
│   └── davu_chinese_original.mp3    # Bản thu gốc của Hoàng Linh
├── output/
│   ├── davu_chorus_56s.mp3          # Đoạn trích âm thanh cao trào (56s)
│   ├── davu_3layer_subtitles.ass    # File phụ đề 3 tầng ASS
│   └── DaVu_Chinese_Version_Master.mp4 # Video thành phẩm hoàn thiện
├── scripts/
│   ├── prepare_audio.py             # Trích xuất và fade audio 56s
│   ├── generate_subtitles.py        # Xuất phụ đề 3 tầng ASS chuẩn tỉ lệ
│   └── render_video.py              # Render toàn bộ visual, waveform, phụ đề
├── specs/
│   └── SPECIFICATION.md             # Đặc tả chi tiết dự án
└── tests/
    ├── test_audio.py                # Kiểm thử chuẩn âm thanh
    ├── test_subtitles.py            # Kiểm thử cấu trúc và nội dung phụ đề
    └── test_video.py                # Kiểm thử video, độ phân giải, bitrate, stream
```

---

## 🚀 Hướng Dẫn Chạy & Kiểm Thử
```bash
# 1. Trích xuất âm thanh 56s
python3 scripts/prepare_audio.py

# 2. Tạo phụ đề ASS 3 tầng
python3 scripts/generate_subtitles.py

# 3. Render video master
python3 scripts/render_video.py

# 4. Chạy kiểm thử tự động
python3 -m unittest discover tests/
```
