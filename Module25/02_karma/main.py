from new_exceptions import *
import random


def it_is_a_life():
    total_karma = 0

    with open('karma.log', 'a', encoding='utf-8') as carma_logs:

        while total_karma < 500:
            total_karma += random.randint(1, 7)
            try:
                if random.randint(1, 10) == 10:
                    raise random.choice(karma_exceptions)
            except KillError:
                carma_logs.write('KillError - you just nearly died. '
                                 'Your carma: {}\n'.format(str(total_karma)))
            except DrunkError:
                carma_logs.write('DrunkError - you just nearly choked. '
                                 'Your carma: {}\n'.format(str(total_karma)))
            except CarCrashError:
                carma_logs.write('CarCrashError - you almost got hit by a car. '
                                 'Your carma: {}\n'.format(str(total_karma)))
            except GluttonyError:
                carma_logs.write('GluttonyError - from gluttony, your heart can barely cope. '
                                 'Your carma: {}\n'.format(str(total_karma)))
            except DepressionError:
                carma_logs.write('DepressionError - you almost ended your life. '
                                 'Your carma: {}\n'.format(str(total_karma)))

    print('Your karma is full')


karma_exceptions = (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError)
it_is_a_life()
