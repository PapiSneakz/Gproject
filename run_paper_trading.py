import yaml
import os
from keep_alive import keep_alive   # 👈 add this
from bot.live import TradingLoop    # 👈 make sure this matches your class name

def main():
    # Start the Replit keep-alive server
    keep_alive()

    # Load config
    cfg_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(cfg_path, "r") as f:
        cfg = yaml.safe_load(f)

    # Start trading loop
    loop = TradingLoop(cfg)
    loop.run()

if __name__ == "__main__":
    main()
