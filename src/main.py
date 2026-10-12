from parser import info_builder, target_handler
import argparse

def main():
    parser = argparse.ArgumentParser(prog="pingwatch", description="Pings websites and returns useful info.")
    parser.add_argument("config", help="File location for config")
    args = parser.parse_args()
    config_path = args.config
    targets = target_handler(config_path)
    
    try:
        info_builder(targets)
    except Exception as e:
        print(f"Fudge! {e}")
        
if __name__ == '__main__':
    main()