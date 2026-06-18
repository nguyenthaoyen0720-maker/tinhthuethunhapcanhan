# Lãi đơn
An = C * (1 + (i / 12) * n)

# Lãi kép
Bn = C * (1 + i / 12) ** n

# Tiền lãi nhận được
lai_don = An - C
lai_kep = Bn - C

# Thuế TNCN (giả định 5% trên tiền lãi)
thue_suat = 0.05
thue_lai_don = lai_don * thue_suat
thue_lai_kep = lai_kep * thue_suat

# Số tiền thực nhận sau thuế
thuc_nhan_lai_don = An - thue_lai_don
thuc_nhan_lai_kep = Bn - thue_lai_kep

st.success("Kết quả tính toán")

st.write(f"📌 Số tiền khách hàng nhận được theo lãi đơn: **{An:,.2f} triệu đồng**")
st.write(f"📌 Thuế TNCN phải nộp (lãi đơn): **{thue_lai_don:,.2f} triệu đồng**")
st.write(f"📌 Số tiền thực nhận sau thuế (lãi đơn): **{thuc_nhan_lai_don:,.2f} triệu đồng**")

st.write(f"📌 Số tiền khách hàng nhận được theo lãi kép: **{Bn:,.2f} triệu đồng**")
st.write(f"📌 Thuế TNCN phải nộp (lãi kép): **{thue_lai_kep:,.2f} triệu đồng**")
st.write(f"📌 Số tiền thực nhận sau thuế (lãi kép): **{thuc_nhan_lai_kep:,.2f} triệu đồng**")
