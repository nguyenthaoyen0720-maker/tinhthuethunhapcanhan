import streamlit as st
st.image("logo.jpg")
st.title("Tính thuế thu nhập cá nhân - Đề tài 7 - Nguyễn Thị Thảo Yên")

thu_nhap = st.number_input(
    "Nhập thu nhập tính thuế (triệu đồng/tháng)",
    min_value=0.0,
    value=10.0
)

if st.button("Tính thuế"):

    if thu_nhap <= 5:
        thue = thu_nhap * 0.05

    elif thu_nhap <= 10:
        thue = 0.25 + (thu_nhap - 5) * 0.10

    elif thu_nhap <= 18:
        thue = 0.75 + (thu_nhap - 10) * 0.15

    elif thu_nhap <= 32:
        thue = 1.95 + (thu_nhap - 18) * 0.20

    elif thu_nhap <= 52:
        thue = 4.75 + (thu_nhap - 32) * 0.25

    elif thu_nhap <= 80:
        thue = 9.75 + (thu_nhap - 52) * 0.30

    else:
        thue = 18.15 + (thu_nhap - 80) * 0.35

    st.success("Kết quả tính toán")
    st.write(f"📌 Thuế TNCN phải nộp: **{thue:.2f} triệu đồng**")
