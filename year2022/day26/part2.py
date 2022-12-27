from year2022.day26.common import decode

# BONUS community task :)
# https://www.reddit.com/r/adventofcode/comments/zv4ixy/my_daughter_made_me_my_own_advent_of_code/


def run(data: list[str], raw_data: list[str], is_test: bool):
    return decode(data[0], "[0-9]")
