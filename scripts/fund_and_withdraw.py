from brownie import FundMe


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"the current entrance fee is {entrance_fee}")
    print("funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def main():
    fund()
