# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 12/6/2019
"""

try:
	print('I am sure no exception is going to occur!')
except Exception:
	print('exception')
else:
	# any code that should only run if no exception occurs in the try,
	# but for which exceptions should NOT be caught
	print('This would only run if no exception occurs. And an error here '
		'would NOT be caught.')
finally:
	print('This would be printed in every case.')

# Output: I am sure no exception is going to occur!
# This would only run if no exception occurs. And an error here would NOT be caught
# This would be printed in every case.
