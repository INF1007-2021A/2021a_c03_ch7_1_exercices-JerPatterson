#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(number: int) -> int:
	if number == 0:
		return 0
	elif number == 1:
		return 1
	else:
		return get_fibonacci_number(number - 1) + get_fibonacci_number(number - 2)
	

def get_fibonacci_sequence(elements: int, sequence: list =[0, 1]) -> list:
	if elements <= 2:
		return sequence[0 : elements]
	if elements == len(sequence):
		return 
	else:
		sequence.append(sequence[len(sequence)-1] + sequence[len(sequence)-2])
		get_fibonacci_sequence(elements, sequence)

	return sequence


def get_sorted_dict_by_decimals(values : dict) -> dict:
	return dict(sorted(values.items(), key=lambda number: number[1]-int(number[1])))


def fibonacci_numbers(length : int) -> int:
	yield 0
	yield 1
	number = 2

	previous_last = 0
	last = 1
	while number != length:
		yield previous_last + last
		value = previous_last + last
		previous_last = last
		last = value
		number += 1


def build_recursive_sequence_generator(first_values : list, fibo_def, sequence_memory : bool =False):
	def recursive_generator(length):
		for value in first_values:
			yield value
		number = len(first_values)
		last_values = deque()
		last_values.extend(first_values)

		if sequence_memory == True:
			sequence = first_values
			while number != length:
				yield fibo_def(last_values)
				sequence.append(fibo_def(last_values))
				last_values.append(fibo_def(last_values))
				last_values.popleft
				number += 1

		elif sequence_memory == False:
			while number != length:
				yield fibo_def(last_values)
				last_values.append(fibo_def(last_values))
				last_values.popleft
				number += 1

	return recursive_generator



if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print(get_fibonacci_sequence(20))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator([2, 1], lambda last_elems: last_elems[-1] + last_elems[-2])
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator([3, 0, 2], lambda last_elems: last_elems[-2] + last_elems[-3])
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator([1, 1], lambda last_elems: last_elems[len(last_elems) - last_elems[len(last_elems) - 1]] 
	+ last_elems[len(last_elems) - last_elems[len(last_elems) - 2]], True)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
