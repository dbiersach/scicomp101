# seq_orf.py

import re

AMINO_ACIDS = {
    ("Ala", "A"): ["GCT", "GCA", "GCC", "GCG"],  # Alanine
    ("Arg", "R"): ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],  # Arginine
    ("Asn", "N"): ["AAT", "AAC"],  # Asparagine
    ("Asp", "D"): ["GAT", "GAC"],  # Aspartic Acid
    ("Cys", "C"): ["TGT", "TGC"],  # Cysteine
    ("Gln", "Q"): ["CAA", "CAG"],  # Glutamine
    ("Glu", "E"): ["GAA", "GAG"],  # Glutamic Acid
    ("Gly", "G"): ["GGT", "GGC", "GGA", "GGG"],  # Glycine
    ("His", "H"): ["CAT", "CAC"],  # Histidine
    ("Ile", "I"): ["ATT", "ATC", "ATA"],  # Isoleucine
    ("Leu", "L"): ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],  # Leucine
    ("Lys", "K"): ["AAA", "AAG"],  # Lysine
    ("Met", "M"): ["ATG"],  # Methionine (Start)
    ("Phe", "F"): ["TTT", "TTC"],  # Phenylalanine
    ("Pro", "P"): ["CCT", "CCC", "CCA", "CCG"],  # Proline
    ("Ser", "S"): ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],  # Serine
    ("Thr", "T"): ["ACT", "ACC", "ACA", "ACG"],  # Threonine
    ("Trp", "W"): ["TGG"],  # Tryptophan
    ("Tyr", "Y"): ["TAT", "TAC"],  # Tyrosine
    ("Val", "V"): ["GTT", "GTC", "GTA", "GTG"],  # Valine
    ("Stop", "0"): ["TAA", "TGA", "TAG"],  # Stop
}


def reverse_complement(seq):
    seq_reverse = ""
    for c in seq[::-1]:
        if c == "C":
            seq_reverse += "G"
        elif c == "G":
            seq_reverse += "C"
        elif c == "A":
            seq_reverse += "T"
        elif c == "T":
            seq_reverse += "A"
    return seq_reverse


def make_codons(seq, offset):
    codons = []
    # Each codon is a grouping of three successive nucleotides,
    # starting at some offset in a DNA/RNA sequence
    # Each codon encodes a specific amino acid
    for i in range(offset, len(seq), 3):
        if i + 3 <= len(seq):
            codons.append(seq[i : i + 3])
    return codons


def find_codon(codon_list, codon):
    try:
        # Get index if this codon appears in the codon list
        idx = codon_list.index(codon)
        return idx
    except ValueError:
        # This codon does not appear in the list
        return -1


def decode_codons(codon_string):
    # Invert AMINO_ACIDS so it is keyed by codon, not amino acid
    inverted_dict = {}
    for k in AMINO_ACIDS:
        for v in AMINO_ACIDS[k]:
            inverted_dict[v] = k
    # Build string of single-letter amino acids based upon each codon
    acids = ""
    for c in codon_string.split():
        # The single letter is the 2nd element in the tuple: [1]
        acids += inverted_dict[c][1]
    # Don't include start and stop codons in amino acid sequence
    acids = acids[1:-1]
    return acids


def get_orf(codon_string, offset):
    # Split sequence into codon list starting at offset
    codon_list = make_codons(codon_string, offset)

    # Find possible index for START codon
    start_idx = find_codon(codon_list, "ATG")
    if start_idx < 0:
        return None

    # Find possible indexes for all three STOP codons
    stop_idexes = [
        find_codon(codon_list, "TAA"),
        find_codon(codon_list, "TAG"),
        find_codon(codon_list, "TGA"),
    ]

    # Remove any STOP codon index that comes before the START index
    stop_idexes[:] = [idx for idx in stop_idexes if idx > start_idx]
    if len(stop_idexes) == 0:
        return None

    # Use the index of the first occuring valid STOP codon
    stop_idx = min(stop_idexes)

    # An empty frame if STOP immediately follows START
    if stop_idx == start_idx + 1:
        return None

    # Build a string of all codons (including START and STOP)
    codon_string = ""
    for idx in range(start_idx, stop_idx + 1):
        codon_string += codon_list[idx] + " "

    # If an ORF exists, also display codons as single character amino acids
    if len(codon_string) > 0:
        codon_string += f" ({decode_codons(codon_string)})"

    return codon_string


def main(file_name):
    with open(file_name, "rb") as f_in:
        print(f"Analyzing {file_name} . . .")

        # Read in text file into an array of file bytes
        f_bytes = bytearray(f_in.read())

        # Enforce uppercase and remove non-letters, convert to UTF-8
        seq = bytearray(f_bytes).decode().upper()
        seq = re.compile("[^A-Z]").sub("", seq)

        # Print the original given sequence
        print(f"Original sequence:  {seq} ")

        # Build and print the reverse compliment of the given sequence
        seq_rc = reverse_complement(seq)
        print(f"Reverse complement: {seq_rc} ")

        # Print any open reading frames in forward sequence
        if s := get_orf(seq, 0):
            print(f"Open Frame +1: {s}")
        if s := get_orf(seq, 1):
            print(f"Open Frame +2: {s}")
        if s := get_orf(seq, 2):
            print(f"Open Frame +3: {s}")

        # Print any open reading frames in reverse compliment of sequence
        if s := get_orf(seq_rc, 0):
            print(f"Open Frame -1: {s}")
        if s := get_orf(seq_rc, 1):
            print(f"Open Frame -2: {s}")
        if s := get_orf(seq_rc, 2):
            print(f"Open Frame -3: {s}")

        return


main("seq2.txt")
