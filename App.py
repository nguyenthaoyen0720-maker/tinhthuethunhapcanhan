import streamlit as st
st.image("Logo.jpg")
st.title("Tính thuế thu nhập cá nhân - Đề tài 7 - Nguyễn Thị Thảo Yên")

# Nhập dữ liệu
thu_nhap = st.number_input(
    "Nhập thu nhập trước thuế (VND)",
    min_value=0.0,
    value=20000000.0
)

so_nguoi_phu_thuoc = st.number_input(
    "Nhập số người phụ thuộc",
    min_value=0,
    value=0
)

if st.button("Tính thuế"):

    # Giảm trừ gia cảnh
    giam_tru_ban_than = 11000000
    giam_tru_phu_thuoc = so_nguoi_phu_thuoc * 4400000

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = thu_nhap - giam_tru_ban_than - giam_tru_phu_thuoc

    if thu_nhap_tinh_thue < 0:
        thu_nhap_tinh_thue = 0

    # Tính thuế TNCN
    if thu_nhap_tinh_thue <= 5000000:
        thue = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 10000000:
        thue = 250000 + (thu_nhap_tinh_thue - 5000000) * 0.10

    elif thu_nhap_tinh_thue <= 18000000:
        thue = 750000 + (thu_nhap_tinh_thue - 10000000) * 0.15

    elif thu_nhap_tinh_thue <= 32000000:
        thue = 1950000 + (thu_nhap_tinh_thue - 18000000) * 0.20

    elif thu_nhap_tinh_thue <= 52000000:
        thue = 4750000 + (thu_nhap_tinh_thue - 32000000) * 0.25

    elif thu_nhap_tinh_thue <= 80000000:
        thue = 9750000 + (thu_nhap_tinh_thue - 52000000) * 0.30

    else:
        thue = 18150000 + (thu_nhap_tinh_thue - 80000000) * 0.35

    st.success("Kết quả tính toán")

    st.write(f"Thu nhập tính thuế: **{thu_nhap_tinh_thue:,.0f} VND**")
    st.write(f"Thuế TNCN phải nộp: **{thue:,.0f} VND**")
