from src.main import is_one_letter_different, find_neighbors, find_chain, load_dictionary
import pytest


def test_words_differ_by_one_letter():
    result = is_one_letter_different('cat', 'cot')

    assert result == True

def test_words_differ_by_two_letters():
    result = is_one_letter_different('cat', 'dog')

    assert result == False

def test_words_are_the_same():
    result = is_one_letter_different('cat', 'cat')

    assert result == False

def test_find_neighbors():
    word_list = ['cat', 'cot', 'dog', 'bat', 'car', 'can']
    result = find_neighbors('cat', word_list)

    assert result == ['cot', 'bat', 'car', 'can']

def test_find_chain_one_step():
    word_list = ['cat', 'cot']
    result = find_chain('cat', 'cot', word_list)

    assert result == ['cat', 'cot']

def test_find_chain_with_more_steps():
    word_list = ['cat', 'cot', 'cog', 'dog', 'bat', 'bog', 'cut']
    result = find_chain('cat', 'dog', word_list)

    assert result == ['cat', 'cot', 'cog', 'dog']

def test_load_dictionary():
    result = load_dictionary('src/ScrabbleWords.txt', 3)
    assert result[0] == 'aah'
    assert len(result) > 100
    assert all(len(w) == 3 for w in result)

def test_find_chain_cat_to_dog():
    dictionary = load_dictionary('src/ScrabbleWords.txt', 3)
    result = find_chain('cat', 'dog', dictionary)
    assert result[0] == 'cat'
    assert result[-1] == 'dog'
    assert len(result) == 4

def test_find_chain_lead_to_gold():
    dictionary = load_dictionary('src/ScrabbleWords.txt', 4)
    result = find_chain('lead', 'gold', dictionary)
    assert result[0] == 'lead'
    assert result[-1] == 'gold'

def test_find_chain_ruby_to_code():
    dictionary = load_dictionary('src/ScrabbleWords.txt', 4)
    result = find_chain('ruby', 'code', dictionary)
    assert result[0] == 'ruby'
    assert result[-1] == 'code'