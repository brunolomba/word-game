import random

end = '\033[m'
red ='\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
magenta ='\033[1;35m'
cyan = '\033[1;36m'

def jogar():

    presentation()

    end_game = '-1'
    while end_game != '0':

        # Escolha das vogais
        chosen_vowels = vowels()

        # Escolha das consoantes
        chosen_consonants = consonants()

        # Juntando letras para jogar
        chosen_letters = join_letters(chosen_vowels, chosen_consonants)

        # Adicionando acentos
        accept_letters = add_accents(chosen_letters)

        # Configurações
        options = '-1'
        chances = number_of_chances(accept_letters)
        hits = 0

        # Looping do Jogo, enquanto a pessoa quiser jogar ou acertar todas as possibilidades da letras
        while chances != 0 and options != '0':

            # Quantas palavras possíveis existem
            print(f'{green}Palavras possíveis = {chances}{end}')

            # Mostrar Letras escolhidas
            print(f'Letras permitidas {yellow}"{chosen_letters}"{end} nas palavras.')

            # Escolha das opções ou chute do jogador
            options = shoot()
            if options == '0':
                break

            # Dica de palavra certa
            elif options == '1':
                correct_word_list = correct_words_current_game(accept_letters)
                hit_words = right_words(accept_letters)
                tip_words(correct_word_list, hit_words)
                continue

            # Adicionando uma letra na sequência
            elif options == '2':
                new_sequence = add_letter(chosen_letters)
                chosen_letters = new_sequence
                accept_letters = add_accents(chosen_letters)
                continue

            # Trocar a sequência de letras por uma nova sequência
            elif options == '3':
                break

            # Verificando letras na palavra
            word_validation = verify_letters(accept_letters, options)
            if word_validation:

                # Verificar palavras aceitas
                correct_word = verify_word(options)

                if correct_word[0] == True:

                    # Salvando as palavras corretas
                    save_correct_word(correct_word)

                    # Contade dos acertos no game atual
                    hits += 1

                    # Atualização das chances
                    chances = number_of_chances(accept_letters)
                    
                else:
                    save_news_words(correct_word)

                print(f'{cyan}Palavras acertadas {hits}{end}')
                print(f'{green}Palavras que você já acertou com essa combinação.{end}')
                correct_word_list = correct_words_current_game(accept_letters)
                show_correct_words_current_game(correct_word_list)

        else:
            print(f'\n{green}P A R A B É N S !!!{end}\nVocê concluiu todas as {green}{number_of_corret_words(accept_letters)} palavras possíveis{end} para a {yellow}sequência de letras "{chosen_letters}"{end}.\n')
            end_game = input(f'''   Pressione {green}ENTER{end} para {green}reiniciar o jogo{end} com uma {yellow}nova sequência de letras{end}\n   ou {red}Digite 0{end} para sair do jogo.\n''')
            options = '-1'

        # Configuração de quando o jogador deseja sair
        if end_game == '0' or options == '0':
            end_game = input(f'{yellow}Digite 1{end} para saber as palavras que você já acertou.\nOu {red}Digite 0{end} para sair.\n')
            if end_game == '1':
                show_all_correct_word()
                break

        # Configuração para não mostrar o ipunt e nem a mensagem de fim de game, quando reinicia a sequência de letras
        else:
            continue
        
    end_messenge(hits, chances)

####   FUNÇÕES     ##########################################################################################################
# Apresetanção do Jogo
def presentation():
    print('\n')
    print(f'{green}Bem vindo!{end} Ao Jogo de Palavras {red}+ DIFíCIL DO MUNDO!{end}')

    print(f'{yellow}OBS: Necessário o uso de acentos para acertar as palavras.{end}\n')

# Sorteando a quantidade e as letras vogais
def vowels():

    valid_letters_vowels = "aeiou"
    chosen_vowels = ''
    amount_vowels = random.randint(2,3)
    count_letters = 0

    while True:
        random_letter = random.choice(valid_letters_vowels)
        if random_letter in chosen_vowels:
            continue
        else:
            chosen_vowels += random_letter
            count_letters += 1
            if count_letters == amount_vowels:
                break

    return chosen_vowels

# Sorteando a quantidade e as letras consoantes
def consonants():

    valid_letters_consonants = "bcdfghjklmnpqrstvwxyz"
    chosen_consonants = ''
    amount_consonants = random.randint(4,6)
    count_letters = 0

    while True:
        random_letter = random.choice(valid_letters_consonants)
        if random_letter in chosen_consonants:
            continue
        else:
            chosen_consonants += random_letter
            count_letters += 1
            if count_letters == amount_consonants:
                break

    return chosen_consonants

# Escolha das letras para jogar
def join_letters(chosen_vowels, chosen_consonants):

    return chosen_vowels + chosen_consonants

# Adicionando um letra escolhida a sequência de letras
def add_letter(chosen_letters):

    new_letter = ''
    while new_letter == '':
        new_letter = input(f"{green}Digite a letra que deseja adicionar:{end}\n")
        if new_letter not in chosen_letters:
            break
        else:
            print(f'A Letra {red}"{new_letter}"{end} já está na sequência, {yellow}escolha outra.{end}')
            new_letter = ''

    if 'a' or 'e' or 'i' or 'o' or 'u' in new_letter:
        new_sequence = new_letter + chosen_letters
        return new_sequence
    else:
        new_sequence = chosen_letters + new_letter
        return new_sequence

def add_accents(chosen_letters):

    accept_letters = chosen_letters

    if 'a' in accept_letters:
        accept_letters += 'áàãâ'

    if 'e' in accept_letters:
        accept_letters += 'éê'

    if 'i' in accept_letters:
        accept_letters += 'íì'

    if 'o' in accept_letters:
        accept_letters += 'óõô'

    if 'u' in accept_letters:
        accept_letters += 'ú'

    return accept_letters

# CHUTE - Palavra que o jogador escolheu
def shoot():
    chute = input(f"""
    {red}Digite 0{end} para sair,
    {green}Digite 1{end} para receber uma palavra certa,
    {magenta}Digite 2{end} para adicionar uma letra na sequência
    {cyan}Digite 3{end} para jogar outra sequência de letras.
    Ou {yellow}Digite sua Palavra.{end}\n""")
    chute = chute.strip()
    return chute

# Verificação das letras na palavra digitada pelo jogador
def verify_letters(accept_letters, kick):
    total_letters = 0

    for letter in kick:
        if letter in accept_letters:
            total_letters += 1
            if total_letters == len(kick):
                return True
        else:
            print(f'{red}Você digitou letras não permitidas.{end}')
            return False

# Verificando palavra no banco de palavras
def verify_word(word):

    with open('correct-words.txt', 'r', encoding="utf8") as archive:
        for line in archive:
            line = line.strip().lower()
            if word.lower() == line:
                print(f'{yellow}Você já acertou essa palavra.{end}')
                return False, word

    with open('accented-words.txt', 'r', encoding="utf8") as archive:
        for line in archive:
            line = line.strip().lower()
            if word.lower() == line:
                print(f'{green}Você acertou a palavra "{word}"{end}')
                return True, word
    
    print(f'A palavra {red}"{word}"{end} não existe em nosso banco de dados')
    return False, word

# Salvar palavra no arquivo "banco de dados"
def save_correct_word(verified_word):

    with open('correct-words.txt', 'a', encoding="utf8") as archive:
        archive.write(verified_word[1].strip() + '\n')

# Salvando palavras verificadas não existentes no banco de dados
def save_news_words(verified_word):

    with open('news-words.txt', 'a', encoding="utf8") as archive:
        archive.write(verified_word[1].strip() + '\n')

# Mostrar palavras acertadas
def show_all_correct_word():
    
    all_correct_word = []

    with open('correct-words.txt', 'r', encoding="utf8") as archive:
        print(f'Palavras acertadas {total_number_of_hits()}')
        for line in archive:
            line = line.strip()
            all_correct_word.append(line)

    # Organizando em ordem alfabética
    all_correct_word.sort()

    if len(all_correct_word) > 0:
        for word in all_correct_word:
            print(word)
    else:
        print(f'{red}Você ainda não acertou nenhuma palavra{end}. {gren}Continue tentando! =){end}')

# Lista de palavras corretas acertadas
def correct_words_current_game(accept_letters):

    correct_words_current_game = []

    with open('correct-words.txt', 'r', encoding="utf8") as archive:
        for line in archive:
            line = line.strip()
            count_letters_word = 0
            for letter in line:
                if letter in accept_letters:
                    count_letters_word += 1
                    if count_letters_word == len(line):
                        correct_words_current_game.append(line)
                        count_letters_word = 0

    # Organizando a lista por ordem alfabética
    correct_words_current_game.sort()

    return correct_words_current_game

# Mostrar palavras acertadas no jogo atual
def show_correct_words_current_game(correct_word_list):

    # Verificando se a lista está vazia para printar
    if len(correct_word_list) > 0:
        for word in correct_word_list:
            print(word)
    else:
        print(f'{red}Você ainda não acertou nenhuma palavra com essa sequência de letras.{end} {green}Continue tentando! =){end}')

# Contagem de todas as palavras
def how_many_words():

    count_words = 0

    with open('accented-words.txt', 'r', encoding="utf8") as archive:
        for line in archive:
            line = line.strip()
            count_words += 1

    return count_words

# Lista das palavras certas
def right_words(accept_letters):

    right_words = []

    with open('accented-words.txt', 'r', encoding="utf8") as archive:
        for line in archive:
            line = line.strip()
            count_letters_word = 0
            for letter in line:
                if letter in accept_letters:
                    count_letters_word += 1
                    if count_letters_word == len(line):
                        right_words.append(line)
                        count_letters_word = 0

    return right_words

# Quantidade de palavras certas
def number_of_corret_words(accept_letters):

    right_words = 0

    with open('correct-words.txt', 'r', encoding="utf8") as archive:
        for line in archive:
            line = line.strip()
            count_letters_word = 0
            for letter in line:
                if letter in accept_letters:
                    count_letters_word += 1
                    if count_letters_word == len(line):
                        right_words += 1
                        count_letters_word = 0

    return right_words

# Número de quantas palavras são possíveis de acertar
def number_of_chances(accept_letters):

    return len(right_words(accept_letters)) - number_of_corret_words(accept_letters)

# Número total de palavras acertadas
def total_number_of_hits():
    count_correct_words = 0

    with open('correct-words.txt', 'r', encoding="utf8") as archive:
        for line in archive:
            line = line.strip()
            count_correct_words += 1
    
    return count_correct_words

# Busca uma palavra na lista de palavras certas e mostra para o jogador
def tip_words(correct_word_list, right_words):

    size_index = len(correct_word_list) - 1
    word = ''

    while True:
        index = random.randint(0, size_index)
        if right_words[index] not in correct_word_list:
            word = right_words[index]
            break
        else:
            continue

    return print(f'A {yellow}DICA{end} da vez é: {green}{word}{end}')

# Quantidade de palavras que faltam
def remaining_words():

    return how_many_words() - total_number_of_hits()

# Mensagem de encerramento do jogo
def end_messenge(hits_of_game, number_of_chances):

    print(f"""{green}Obrigado por jogar! =){end}\nVocê acertou {green}{hits_of_game}{end} de {green}{number_of_chances}{end} possíveis combinações \n
No {green}TOTAL{end} você já acertou {green}{total_number_of_hits()}{end} de {green}{how_many_words()}{end}. Faltam {yellow}{remaining_words()}{end} Palavras.""")

if __name__ == '__main__':
    jogar()