import os
from pathlib import Path
import subprocess
import asyncio

DIR_DATA = Path().cwd().resolve() / "data"
DIR_DATA.mkdir(parents=True, exist_ok=True)

async def callback(command: str = ""):
    retries = 0

    if len(command) == 0:
        return False

    try:
        subprocess.run([command], timeout= 3600 * 3,shell=True)

        print("Completed running:")
        print(command)
        print()
        return True
    except:
        return False


async def main():
    commands = []
    with open(DIR_DATA / "podaac_data_subscriber_prompts_v3.txt", "r") as prompts:
        commands = prompts.readlines()
        prompts.close()
        
    await asyncio.gather(
        callback(commands[0]), 
        callback(commands[1]),
        callback(commands[2]), 
        callback(commands[3]), 
        callback(commands[4]), 
        callback(commands[5]), 
        callback(commands[6]), 
        callback(commands[7]), 
        )


if __name__ == "__main__":
    asyncio.run(main())