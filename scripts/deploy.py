from brownie import FundMe, MockV3Aggregator, config, accounts, network
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"Active network is {network.show_active()}")
        print("deploying mocks...")
        MockV3Aggregator.deploy(18, 2000000000000000000000, {"from": account})

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=True,
    )
    print(f"Contracts are deployed to {fund_me.address}")


def main():
    deploy_fund_me()
