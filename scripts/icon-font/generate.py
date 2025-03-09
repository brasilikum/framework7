# Font generation script from Ionicons
# https://github.com/driftyco/ionicons/
# http://ionicons.com/

from subprocess import call
import os

BUILDER_PATH = os.path.dirname(os.path.abspath(__file__))

def main():
  generate_font_files()

def generate_font_files():
  print("Generate Fonts")
  cmd = f"fontforge -script {BUILDER_PATH}/generate_font.py"
  call(cmd, shell=True)

if __name__ == "__main__":
  main()
