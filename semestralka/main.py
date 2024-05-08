from djCalculator import DjCalculator

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
    
def run(input_file: str, output_file: str) -> None:
    calculator = DjCalculator()
    with open(input_file, "r") as input:
        with open(output_file, "w") as output:
            for input_line in input:
                input_line = input_line.rstrip()
                try:
                    result = f"{input_line} -> {calculator.calculate(input_line)}\n"
                except Exception as e:
                    result = f"{input_line} -> {e}\n"
                finally:
                    # print result
                    print(result)
                    # write output into output file
                    output.write(result + "\n")              

if __name__ == "__main__":
    run(INPUT_FILE, OUTPUT_FILE)
    print("------------------------------------Done------------------------------------")