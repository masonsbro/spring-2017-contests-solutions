import requests
import re
import random

CODES_FILE = "airport_codes.txt"

def scrape_html_codes():
    html = requests.get("http://www.airportcodes.org/")

    pattern = "\((.{3})\)"  # Find 3-char parenthesized strings
    codes   = re.findall(pattern, html.text)
    codes   = set(codes)

    for code in codes:
        for x in code:
            assert('A' <= x <= 'Z')

    return codes

def straightforward():
    priority = ["FKL","ABL"]
    input    = {"FKB","ABM","ABK","ABL","ABJ","FKQ","FKS","FKL","ABI"}
    output   = sorted(priority)
    output.extend(sorted((x for x in input if x not in priority)))
    return priority, input, output

def ordering():
    with open(CODES_FILE, "r") as f:
        all_codes = f.read().split()

    priority = {code for code in all_codes if code != "AAC"}
    random.seed(1)
    input    = random.sample(all_codes, len(all_codes))

    # All input should be in sorted order, except 'AAC' should be at the end
    output   = sorted(all_codes)[1:]
    output.append("AAC")

    return priority, input, output

def no_priority_codes():
    with open(CODES_FILE, "r") as f:
        all_codes = f.read().split()

    priority = {}
    random.seed(1)
    input    = random.sample(all_codes, len(all_codes))
    output   = sorted(input)

    return priority, input, output

def all_priority_codes():
    with open(CODES_FILE, "r") as f:
        all_codes = f.read().split()

    random.seed(5)
    priority = random.sample(all_codes, len(all_codes))
    random.seed(1)
    input    = random.sample(all_codes, len(all_codes))
    output   = sorted(input)

    return priority, input, output

def no_input_codes():
    with open(CODES_FILE, "r") as f:
        all_codes = f.read().split()

    random.seed(5)
    priority = random.sample(all_codes, len(all_codes))
    input    = {}
    output   = {}

    return priority, input, output

TEST_CASE_FNS = [straightforward, no_input_codes, ordering, no_priority_codes, all_priority_codes]

if __name__ == "__main__":
    # Scrape
    codes = scrape_html_codes()
    codes = sorted(codes)
    with open(CODES_FILE, "w") as f:
        for code in codes:
            f.write("{}\n".format(code))

    # Populate test cases
    f_in  = open("contest.in", "w")
    f_out = open("contest.out", "w")

    f_in.write("{}\n".format(len(TEST_CASE_FNS)))

    for fn in TEST_CASE_FNS:
        priority_codes, input_codes, output_codes = fn()

#         print("Priority codes, input codes, output codes:")
#         print(priority_codes)
#         print(input_codes)
#         print(output_codes)

        assert(len(input_codes) == len(output_codes))

        f_in.write("{}\n".format(len(priority_codes)))
        for code in priority_codes:
            f_in.write("{}\n".format(code))

        f_in.write("{}\n".format(len(input_codes)))
        for code in input_codes:
            f_in.write("{}\n".format(code))

        for code in output_codes:
            f_out.write("{}\n".format(code))

    f_in.close()
    f_out.close()
