
import re

class CNFConverter:
    def __init__(self, custom_variable_map=None):
        self.variable_map = custom_variable_map or {}  # To store the mapping of variables to unique numbers
        self.clauses = []  # To store the CNF clauses

        if self.variable_map:
            self.var_counter = max(self.variable_map.values()) + 1
        else:
            self.var_counter = 1    # To assign unique numbers to variables

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

    def xnor_gate2(self, input1, input2, output):
    
        in1, in2, out = map(self.get_variable_num, [input1, input2, output])
        
        self.add_clause([out, -in1, in2])     
        self.add_clause([out, in1, -in2])     
        self.add_clause([-out, in1, in2])      
        self.add_clause([-out, -in1, -in2])    

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



# Example input circuit including NAND and XOR gates
input_circuit = """



not(B0,B0')
not(B1,B1')
not(B2,B2')
not(B3,B3')

not(M,M')

and2(A0,A0,Z1)
and2(B0,S0,Z2)
and2(B0',S1,Z3)
and3(B0',S2,A0,Z4)
and3(B0,A0,S3,Z5)
and2(A1,A1,Z6)
and2(B1,S0,Z7)
and2(B1',S1,Z8)
and3(A1,B1',S2,Z9)
and3(A1,B1,S3,Z10)
and2(A2,A2,Z11)
and2(B2,S0,Z12)
and2(B2',S1,Z13)
and3(A2,B2',S2,Z14)
and3(A2,B1,S3,Z15)
and2(A3,A3,Z16)
and2(B3,S0,Z17)
and2(B3',S1,Z18)
and3(A3,B3',S2,Z19)
and3(A3,B3,S3,Z20)

nor3(Z1,Z2,Z3,Y1)
nor2(Z4,Z5,Y2)
nor3(Z6,Z7,Z8,Y3)
nor2(Z9,Z10,Y4)
nor3(Z11,Z12,Z13,Y5)
nor2(Z14,Z15,Y6)
nor3(Z16,Z17,Z18,Y7)
nor2(Z19,Z20,Y8)

xor2(Y1,Y2,X1)
xor2(Y3,Y4,X2)
xor2(Y5,Y6,X3)
xor2(Y7,Y8,X4)

nand2(M',C',W1)
and2(M',Y1,W2)
and3(M',C',Y2,W3)
and2(M',Y3,W4)
and3(M',Y4,Y1,W5)
and4(M',C',Y4,Y2,W6)
and2(M',Y5,W7)
and3(M',Y6,Y3,W8)
and4(M',Y1,Y4,Y6,W9)
and5(M',C',Y2,Y6,Y4,W10)

nor2(W2,W3,V1)
nor3(W4,W5,W6,V2)
nor4(W7,W8,W9,W10,V3)

xor2(X1,W1,F0)
xor2(X2,V1,F1)
xor2(X3,V2,F2)
xor2(X4,V3,F3)

















not(B0, fB0')
not(B1, fB1')
not(B2, fB2')
not(B3, fB3')

not(M, fM')

and2(A0, A0, fZ1)
and2(B0, S0, fZ2)
and2(B0', S1, fZ3)
and3(B0', S2, A0, fZ4)
and3(B0, A0, S3, fZ5)
and2(A1, A1, fZ6)
and2(B1, S0, fZ7)
and2(B1', S1, fZ8)
and3(A1, B1', S2, fZ9)
and3(A1, B1, S3, fZ10)
and2(A2, A2, fZ11)
and2(B2, S0, fZ12)
and2(B2', S1, fZ13)
and3(A2, B2', S2, fZ14)
and3(A2, B2, S3, fZ15)
and2(A3, A3, fZ16)
and2(B3, S0, fZ17)
and2(B3', S1, fZ18)
and3(A3, B3', S2, fZ19)
and3(A3, B3, S3, fZ20)


nor3(fZ1,fZ2,fZ3,fY1)
nor2(fZ4,fZ5,fY2)
nor3(fZ6,fZ7,fZ8,fY3)
nor2(fZ9,fZ10,fY4)
nor3(fZ11,fZ12,fZ13,fY5)
nor2(fZ14,fZ15,fY6)
nor3(fZ16,fZ17,fZ18,fY7)
nor2(fZ19,fZ20,fY8)

xor2(fY1,fY2,fX1)
xor2(fY3,fY4,fX2)
xor2(fY5,fY6,fX3)
xor2(fY7,fY8,fX4)

nand2(fM',C',fW1)
and2(fM',fY1,fW2)
and3(fM',C',fY2,fW3)
and2(fM',fY3,fW4)
and3(fM',fY4,fY1,fW5)
and4(fM',C',fY4,fY2,fW6)
and2(fM',fY5,fW7)
and3(fM',fY6,fY3,fW8)
and4(fM',fY1,fY4,fY6,fW9)
and5(fM',C',fY2,fY6,fY4,fW10)

nor2(fW2,fW3,fV1)
nor3(fW4,fW5,fW6,fV2)
nor4(fW7,fW8,fW9,fW10,fV3)

xor2(fX1,fW1,fF0)
xor2(fX2,fV1,fF1)
xor2(fX3,fV2,fF2)
xor2(fX4,fV3,fF3)







xor2(F0,fF0,alpha)
xor2(F1,fF1,beta)
xor2(F2,fF2,gamma)
xor2(F3,fF3,delta)
or2(alpha,beta,kk)
or2(kk,gamma,kkk)
or2(kkk,delta,root)















"""

# Initialize the CNFConverter
cnf_converter = CNFConverter()

# Parse the circuit and generate CNF
cnf_converter.parse_input(input_circuit)
cnf_output = cnf_converter.generate_cnf()

# Print the CNF Output
print("CNF Output:\n", cnf_output)

# Print the variable mapping
print("\nVariable Mapping:\n", cnf_converter.get_variable_mapping())