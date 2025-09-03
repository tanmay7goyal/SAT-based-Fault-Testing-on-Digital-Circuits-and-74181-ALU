import re

class CNFConverter:
    def __init__(self, custom_variable_map=None):  # Fix typo here: _init_ -> __init__
        self.variable_map = custom_variable_map or {}  # To store the mapping of variables to unique numbers
        self.clauses = []  # To store the CNF clauses

        if self.variable_map:
            self.var_counter = max(self.variable_map.values()) + 1
        else:
            self.var_counter = 1    # To assign unique numbers to variables

    # The rest of the code remains unchanged.


    def get_variable_num(self, var):
        """Map a variable to a unique number."""
        if var not in self.variable_map:
            self.variable_map[var] = self.var_counter
            self.var_counter += 1
        return self.variable_map[var]

    def add_clause(self, clause):
        """Add a clause to the CNF list."""
        self.clauses.append(clause)

    def and_gate2(self, input1, input2, output):
        """Convert AND gate to CNF."""
        in1, in2, out = map(self.get_variable_num, [input1, input2, output])
        self.add_clause([out, -in1, -in2])
        self.add_clause([-out, in1])
        self.add_clause([-out, in2])

    def and_gate3(self, input1, input2,input3, output):
        """Convert AND gate 3 input to CNF."""
        in1, in2,in3, out = map(self.get_variable_num, [input1, input2,input3, output])
        self.add_clause([out, -in1, -in2, -in3])
        self.add_clause([-out, in1])
        self.add_clause([-out, in2])
        self.add_clause([-out, in3])

    def and_gate4(self, input1, input2,input3,input4, output):
        """Convert AND gate 4 input to CNF."""
        in1, in2,in3,in4, out = map(self.get_variable_num, [input1, input2, input3, input4, output])
        self.add_clause([out, -in1, -in2, -in3, -in4])
        self.add_clause([-out, in1])
        self.add_clause([-out, in2])
        self.add_clause([-out, in3])
        self.add_clause([-out, in4])

    def and_gate5(self, input1, input2,input3,input4,input5, output):
        """Convert AND gate 4 input to CNF."""
        in1, in2,in3,in4,in5, out = map(self.get_variable_num, [input1, input2, input3, input4,input5, output])
        self.add_clause([out, -in1, -in2, -in3, -in4, -in5])
        self.add_clause([-out, in1])
        self.add_clause([-out, in2])
        self.add_clause([-out, in3])
        self.add_clause([-out, in4])
        self.add_clause([-out, in5])

    def or_gate2(self,  input1, input2, output):
        """Convert OR gate to CNF."""
        in1, in2, out = map(self.get_variable_num, [input1, input2, output])
        self.add_clause([-out, in1, in2])
        self.add_clause([out, -in1])
        self.add_clause([out, -in2])

    def not_gate(self, input1,output):
        """Convert NOT gate to CNF."""
        in1, out = map(self.get_variable_num, [input1, output])
        self.add_clause([out, in1])
        self.add_clause([-out, -in1])

    def buffer_gate(self,input1,output):
        """Convert Buffer/pass gate to CNF."""
        in1, out = map(self.get_variable_num, [input1, output])
        self.add_clause([-out, in1])
        self.add_clause([out, -in1])

    def nand_gate2(self,  input1, input2, output):
        """Convert NAND gate to CNF."""
        in1, in2, out = map(self.get_variable_num, [input1, input2, output])
        self.add_clause([-out, -in1, -in2])
        self.add_clause([out, in1])
        self.add_clause([out, in2])

    def nor_gate2(self, input1, input2, output):
        """Convert NOR gate to CNF."""
        in1, in2, out = map(self.get_variable_num, [input1, input2, output])
        self.add_clause([out, -in1, -in2])
        self.add_clause([-out, in1])
        self.add_clause([-out, in2])


    def nor_gate3(self, input1, input2,input3, output):
        """Convert NOR gate to CNF."""
        in1, in2, in3, out = map(self.get_variable_num, [input1, input2, input3, output])
        self.add_clause([out, -in1, -in2, -in3])
        self.add_clause([-out, in1])
        self.add_clause([-out, in2])
        self.add_clause([-out, in3])

    def nor_gate4(self, input1, input2,input3, input4, output):
        """Convert NOR gate to CNF."""
        in1, in2, in3, in4, out = map(self.get_variable_num, [input1, input2, input3, input4, output])
        self.add_clause([out, -in1, -in2, -in3, -in4])
        self.add_clause([-out, in1])
        self.add_clause([-out, in2])
        self.add_clause([-out, in3])
        self.add_clause([-out, in4])


    def xor_gate2(self,  input1, input2, output):
        """Convert XOR gate to CNF."""
        in1, in2, out = map(self.get_variable_num, [input1, input2, output])
        self.add_clause([-out, -in1, -in2])
        self.add_clause([-out, in1, in2])
        self.add_clause([out, -in1, in2])
        self.add_clause([out, in1, -in2])

    def parse_input(self, input_str):
        """Parse the input string to identify gates and their variables."""
        lines = input_str.strip().splitlines()
        for line in lines:
            match = re.match(r"(\w+)\(([^)]+)\)", line.strip())
            if match:
                gate_type = match.group(1).strip().lower()
                variables = [var.strip() for var in match.group(2).split(',')]
                if gate_type == 'and2' and len(variables) == 3:
                    self.and_gate2(*variables)
                elif gate_type == 'and3' and len(variables) == 4:
                    self.and_gate3(*variables)
                elif gate_type == 'and4' and len(variables) == 5:
                    self.and_gate4(*variables)
                elif gate_type == 'and5' and len(variables) == 6:
                    self.and_gate5(*variables)
                elif gate_type == 'or2' and len(variables) == 3:
                    self.or_gate2(*variables)
                elif gate_type == 'not' and len(variables) == 2:
                    self.not_gate(*variables)
                elif gate_type == 'buffer' and len(variables) == 2:
                    self.buffer_gate(*variables)
                elif gate_type == 'nand2' and len(variables) == 3:
                    self.nand_gate2(*variables)
                elif gate_type == 'nor2' and len(variables) == 3:
                    self.nor_gate2(*variables)
                elif gate_type == 'nor3' and len(variables) == 4:
                    self.nor_gate3(*variables)
                elif gate_type == 'nor4' and len(variables) == 5:
                    self.nor_gate4(*variables)
                elif gate_type == 'xor2' and len(variables) == 3:
                    self.xor_gate2(*variables)
                else:
                    print(f"Invalid gate or parameters: {line}")

    def generate_cnf(self):
        """Output CNF clauses in DIMACS format (numeric)."""
        num_vars = len(self.variable_map)
        num_clauses = len(self.clauses)
        result = [f"p cnf {num_vars} {num_clauses}"]
        for clause in self.clauses:
            result.append(" ".join(map(str, clause)) + " 0")
        return "\n".join(result)

    def generate_cnf(self, filename=None):
        """Output CNF clauses in DIMACS format (numeric), optionally writing to a file."""
        num_vars = len(self.variable_map)
        num_clauses = len(self.clauses)
        result = [f"p cnf {num_vars} {num_clauses}"]
        for clause in self.clauses:
            result.append(" ".join(map(str, clause)) + " 0")

        return "\n".join(result)


    def get_variable_mapping(self):
        mapping = "\n".join(f"{var} -> {num}" for var, num in self.variable_map.items())
        return mapping

input_circuit = """
nand2(A, B, E)
nand2(A, E, H)
nand2(B, E, I)
nand2(H, I, J)
nand2(A, F', H')
nand2(H', I, J')
xor2(J, J', K)
"""

# Initialize the CNFConverter with the custom variable map
cnf_converter = CNFConverter()

# Parse the circuit and generate CNF
cnf_converter.parse_input(input_circuit)
cnf_output = cnf_converter.generate_cnf()

# Print the CNF Output
print("CNF Output:\n", cnf_output)

# Print the variable mapping
print("\nVariable Mapping:\n", cnf_converter.get_variable_mapping())