import streamlit as st
st.image("Logo.jpg")
st.title("Tính thuế thu nhập cá nhân - Đề tài 7 - Nguyễn Thị Thảo Yên")

# ==========================
# Nhập dữ liệu
# ==========================

thu_nhap = st.number_input(
    "Nhập thu nhập trước thuế (VND)",
    min_value=0.0,
    value=20_000_000.0,
    step=100_000.0,
    format="%.2f"
)

so_nguoi_phu_thuoc = st.number_input(
    "Nhập số người phụ thuộc",
    min_value=0,
    value=0,
    step=1
)

if st.button("Tính thuế"):

    # ==========================
    # Theo quy định từ 01/01/2026
    # ==========================
    giam_tru_ban_than = 15_500_000
    giam_tru_phu_thuoc = so_nguoi_phu_thuoc * 6_200_000

    # Giả sử toàn bộ thu nhập là mức lương đóng BH bắt buộc
    bao_hiem = thu_nhap * 0.105

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = (
        thu_nhap
        - bao_hiem
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
    )

    if thu_nhap_tinh_thue < 0:
        thu_nhap_tinh_thue = 0

    # ==========================
    # Biểu thuế lũy tiến từng phần
    # ==========================

    if thu_nhap_tinh_thue <= 5_000_000:
        thue = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 10_000_000:
        thue = 250_000 + (thu_nhap_tinh_thue - 5_000_000) * 0.10

    elif thu_nhap_tinh_thue <= 18_000_000:
        thue = 750_000 + (thu_nhap_tinh_thue - 10_000_000) * 0.15

    elif thu_nhap_tinh_thue <= 32_000_000:
        thue = 1_950_000 + (thu_nhap_tinh_thue - 18_000_000) * 0.20

    elif thu_nhap_tinh_thue <= 52_000_000:
        thue = 4_750_000 + (thu_nhap_tinh_thue - 32_000_000) * 0.25

    elif thu_nhap_tinh_thue <= 80_000_000:
        thue = 9_750_000 + (thu_nhap_tinh_thue - 52_000_000) * 0.30

    else:
        thue = 18_150_000 + (thu_nhap_tinh_thue - 80_000_000) * 0.35

    # Thu nhập sau thuế
    thu_nhap_sau_thue = thu_nhap - bao_hiem - thue

    # ==========================
    # Hiển thị kết quả
    # ==========================

    st.success("Kết quả tính toán")

    st.write(f"📌 Thu nhập trước thuế: **{thu_nhap:,.0f} VND**")
    st.write(f"📌 Giảm trừ bản thân: **{giam_tru_ban_than:,.0f} VND**")
    st.write(f"📌 Giảm trừ người phụ thuộc: **{giam_tru_phu_thuoc:,.0f} VND**")
    st.write(f"📌 Bảo hiểm bắt buộc (10.5%): **{bao_hiem:,.0f} VND**")
    st.write(f"📌 Thu nhập tính thuế: **{thu_nhap_tinh_thue:,.0f} VND**")
    st.write(f"📌 Thuế TNCN phải nộp: **{thue:,.0f} VND**")
    st.write(f"📌 Thu nhập sau thuế: **{thu_nhap_sau_thue:,.0f} VND**")
