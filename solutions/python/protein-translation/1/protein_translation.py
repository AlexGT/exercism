def proteins(strand):
    protein_dict = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP',
    }
    codon_length = 3
    codon_list = []
    for i in range(0, len(strand), 3):
        codon = protein_dict[strand[i:i+codon_length]]
        if codon != 'STOP':
            codon_list.append(codon)
        else:
            break

    return codon_list
