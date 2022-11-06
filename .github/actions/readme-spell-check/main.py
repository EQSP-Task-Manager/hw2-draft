import os
import sys
import subprocess
import argparse

from io import TextIOWrapper
from dataclasses import dataclass

from markdown import markdown
from bs4 import BeautifulSoup

ACCEPTED_WORDS_FILE_PATH = '/accepted-words.txt'


@dataclass
class LineReport:
    num: int
    words: list[str]


@dataclass
class Report:
    lines: list[LineReport]

    def to_markdown(self) -> str:
        result = []
        for line in self.lines:
            result.append(f'**{line.num}**: {" ".join(line.words)}')
        return '\n'.join(result)


def main():
    args_parser = argparse.ArgumentParser(description='README.md spell checker')
    args_parser.add_argument('--path', type=str, default='README.md', help='Path to README.md file')
    args = args_parser.parse_args()

    if not os.path.exists(args.path):
        print('The path specified does not exist')
        sys.exit(1)

    report = _get_report(args.path)
    if len(report.lines) > 0:
        print('## Misspelled words')
        print(report.to_markdown())
        sys.exit(1)
    print('## No misspelled words)')


def _get_report(file_path: str) -> Report:
    line_reports = []
    with open(file_path, 'r') as file:
        for num, line in enumerate(file):
            misspelled_words = _get_misspelled_words(line)
            if len(misspelled_words) > 0:
                line_report = LineReport(num=num + 1, words=misspelled_words)
                line_reports.append(line_report)
    return Report(lines=line_reports)


def _get_misspelled_words(text: str) -> list[str]:
    with open(ACCEPTED_WORDS_FILE_PATH, 'r') as file:
        accepted_words = set(file.read().split('\n'))

    process = subprocess.run(
        f'echo \'{text}\' | aspell --lang en_US --mode markdown list',
        shell=True, check=True, text=True, stdout=subprocess.PIPE
    )
    result = []
    words = set()
    for word in process.stdout.split('\n'):
        if len(word) > 0 and word not in words and word not in accepted_words:
            words.add(word)
            result.append(word)
    return result


def _get_raw_text_from_markdown_file(file: TextIOWrapper) -> str:
    markdown_text = file.read()
    html_text = markdown(markdown_text)
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup.get_text()


if __name__ == '__main__':
    main()
