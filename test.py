import pyupbit

access = "Qk55ExRO6W7H1mlHvADJmYI2aTUkCApTLze0xxDx"          # 본인 값으로 변경
secret = "UIBWoZJ8qouXemFzcSx25r0nbgkJbNfZzbI5nrVw"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회