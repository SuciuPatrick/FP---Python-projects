from Domain.Rental import *
import datetime


class rentalValidator:
	@staticmethod
	def validate(rental, rentalRepo):
		if rental.rental_id == '':
			raise ValueError("Not a valid id. It can't be empty")
		
		if isinstance(rental, Rental) is False:
			raise TypeError("It is not a rental object.")
		_errors = []
		if rentalRepo.findByID(rental.rental_id):
			_errors.append("Rental ID already taken")
		for rentMov in rentalRepo.getList():
			if rentMov.client.id == rental.client.id:
				if rentMov.returnedDate > rentMov.dueDate or rentMov.returnedDate == datetime.date(1, 1, 1):
					_errors.append("Invalid client for rental")
		for rentMov in rentalRepo.getList():
			if rentMov.movie.id == rental.movie.id:
				if rentMov.returnedDate > rental.rentedDate or rentMov.returnedDate == datetime.date(1, 1, 1):
					_errors.append("Unavailable movie.")
		if rental.rentedDate > rental.dueDate:
			_errors.append("RentedDate must be lower than dueDate.")

		if len(_errors) > 0:
			index = 0
			while index < len(_errors):
				print(_errors[index])
				index += 1

	@staticmethod
	def validateReturn(rentalRepo, an_id, returnedDate):
		c = 0
		for rental in rentalRepo.getList():
			if rental.movie.id == an_id:
				c = 1
				if returnedDate < rental.rentedDate:
					raise ValueError("Back to the future")
		if c == 0:
			print("ID not found")