import os
import openai
import sys
import time
import random
import argparse

from decouple import Config, RepositoryEnv

DOTENV_FILE = './.env'
env_config = Config(RepositoryEnv(DOTENV_FILE))
openai.api_key = env_config.get('OPENAI_API_KEY')

# this will read the argument for temperature
parser = argparse.ArgumentParser()
parser.add_argument('--temperature', type=float, default=0.5)
parser.add_argument('--max_tokens', type=int, default=100)

def write_one_character_at_a_time(text):
    # generate a list of random numbers between 0.01 and 0.1
    random_numbers = [random.uniform(0.001, 0.1) for i in range(len(text))]
    for i, character in zip(range(len(text)), text):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(random_numbers[i])
        
while(True):
    print("Enter your prompt: ")
    prompt = input()
    print("\nOpenAI Completion endpoint response:")
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=parser.parse_args().temperature,
        max_tokens=parser.parse_args().max_tokens,
        presence_penalty=0.6,
    )
    write_one_character_at_a_time(response.choices[0].text)
    print("\n")
  
