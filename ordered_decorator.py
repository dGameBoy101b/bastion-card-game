from functools import total_ordering
from types import NotImplementedType
from typing import Any, Callable, Iterable, Tuple, Type

class Ordering(Tuple):
	def compare_indices(self, a:Any, b:Any) -> int|NotImplementedType:
		'''
		return:
			< 0: `a` comes before `b`
			0: `a` equals `b`
			> 0: `a` comes after `b`
			NotImplemented: `a` or `b` are not in the ordering
		'''
		try:
			a_index = self.index(a)
			b_index = self.index(b)
		except ValueError:
			return NotImplemented
		return a_index - b_index

def ordered[T](order: Iterable[T]):
	'''
	Adds rich comparison dunder methods to class that follows the given order.
	'''
	ordering = Ordering(order)
	def add_order(cls: Type[T]) -> Type[T]:
		def create_indice_comparison(check_difference:Callable[[int], bool]) -> Callable[[T, Any], bool|NotImplementedType]:
			def compare_indices(self:T, other:Any)->bool|NotImplementedType:
				nonlocal ordering, check_difference
				difference = ordering.compare_indices(self, other)
				if difference is NotImplemented:
					return NotImplemented
				return check_difference(difference)
			return compare_indices
		cls.__lt__ = create_indice_comparison(lambda diff: diff < 0)
		cls = total_ordering(cls)
		return cls
	return add_order