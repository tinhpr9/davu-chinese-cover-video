# Specification: Dạ Vũ (夜舞) - Chinese Version Full Master Video

## 1. Overview
- **Project**: Chinese version cover video of Vietnamese mega-hit "Dạ Vũ" (Tăng Duy Tân).
- **Vocalist**: Professional studio master vocal by Chinese artist Hoàng Linh (黄龄).
- **Format**: Vertical short-form / full-length video (1080x1920, 9:16), 30 FPS.
- **Duration**: Full Song 200.088 seconds (~3 minutes 20 seconds).
- **Visual Style**: Classical Chinese cổ trang maiden playing Pipa in a moonlit antique pavilion with glowing lanterns, cinematic Ken Burns motion, 3-layer synchronized lyrics.

## 2. Visual Architecture
- **Subject**: Ultra-detailed vertical 1080x1920 portrait of an ethereal Chinese maiden in silk Hanfu robes holding a traditional Pipa (`assets/chinese_beauty_pipa.jpg`).
- **Motion**: Subtle continuous Ken Burns push-in zoom (`zoompan`, z: 1.0 -> 1.08 over 200s).
- **Composition**:
  - Top header (Y: ~150 - 270): Title and artist branding.
  - Middle: Maiden's expressive face, instrument, and courtyard atmosphere.
  - Lower area (Y: ~1350 - 1650): 3-Layer subtitles with high contrast drop shadows for flawless readability.

## 3. Subtitle Architecture (3-Layer Full Song Synchronized)
- Format: Advanced SubStation Alpha (`.ass`), PlayResX=1080, PlayResY=1920.
- Timing Verification: Frame-by-frame verified via OCR against the official release video.
- Complete Song Breakdown:
  1. `00:00 - 00:23.00`: Intro Guzheng & Dizi flute
  2. `00:23.00 - 00:27.00`: 恰好照在夜风微凉的晚上 (Vừa lúc chiếu vào cơn gió lạnh buổi đêm)
  3. `00:27.00 - 00:31.50`: 树影灯影都随月影在摇晃 (Bóng cây ánh đèn cũng đung đưa theo ánh trăng)
  4. `00:31.50 - 00:36.50`: 晃得心中所想无处去隐藏 (Khiến tâm sự trong lòng chẳng nơi giấu kín)
  5. `00:36.50 - 00:41.00`: 勾勒出被遗忘的念念不忘 (Phác họa lại những vương vấn ngỡ đã lãng quên)
  6. `00:41.00 - 00:45.50`: 回想起已寻常的极不寻常 (Hồi tưởng lại những thứ tầm thường nay lại chẳng tầm thường)
  7. `00:45.50 - 00:49.50`: 冰凉的是否还能变得滚烫 (Lạnh lẽo liệu chăng có thể trở lại nóng bỏng?)
  8. `00:49.50 - 00:53.50`: 心中某个地方 也曾照进一道光 (Đâu đó trong tim cũng từng được ánh sáng soi rọi)
  9. `00:53.50 - 00:57.50`: 谁翻云覆雨冷不防 (Là ai bất chợt tạo nên phong ba khôn lường)
  10. `00:57.50 - 01:03.00`: 卷起时光 再轻放下 (Cuộn thời gian lên rồi nhẹ nhàng buông xuống)
  11. `01:03.00 - 01:05.50`: 我不由自主去回望 (Em không kìm được lại ngoảnh đầu nhìn lại)
  12. `01:05.50 - 01:13.00`: 那些时光 都太漫长 终难忘 (Những tháng ngày ấy quá đỗi dài lâu, rốt cuộc khó lòng quên)
  13. `01:13.00 - 01:21.00`: 随风起舞 叹这长夜 (Vũ điệu cùng gió, thở than giữa đêm trường...)
  14. `01:21.00 - 01:38.00`: Drop Beat 1
  15. `01:38.00 - 01:49.00`: Guzheng Interlude
  16. `01:49.00 - 01:54.00`: 都怪我还想 沉溺于你的假象 (Đều tại em vẫn mơ tưởng, chìm đắm trong ảo ảnh của người)
  17. `01:54.00 - 02:00.00`: 就让回忆随时间流淌 可前路悠长 (Cứ để hồi ức trôi theo năm tháng, dẫu chặng đường phía trước xa xôi)
  18. `02:00.00 - 02:05.00`: 到处都是过往的形状 (Nơi nơi đều ngập tràn hình bóng của quá khứ)
  19. `02:05.00 - 02:09.50`: 勾勒出被遗忘的念念不忘
  20. `02:09.50 - 02:14.00`: 回想起已寻常的极不寻常
  21. `02:14.00 - 02:17.50`: 冰凉的是否还能变得滚烫
  22. `02:17.50 - 02:22.00`: 心中某个地方 也曾照进一道光
  23. `02:22.00 - 02:26.00`: 谁翻云覆雨冷不防
  24. `02:26.00 - 02:31.00`: 卷起时光 再轻放下
  25. `02:31.00 - 02:34.50`: 我不由自主去回望
  26. `02:34.50 - 02:42.00`: 那些时光 都太漫长 终难忘
  27. `02:42.00 - 02:50.00`: 随风起舞 叹这长夜
  28. `02:50.00 - 03:12.00`: Drop Beat 2
  29. `03:12.00 - 03:20.08`: Outro Fade

## 4. Deliverables & Device Deployment
- `output/DaVu_Chinese_Version_FULL_Master.mp4`: Full 3m20s video (1080x1920, 30fps).
- Device destination: `/storage/emulated/0/DCIM/Camera/` & `/storage/emulated/0/Movies/`.
