from steps.compress import compress
from steps.convert import convert
from steps.split512 import split512
from steps.schedule import schedule
from helpers.constants import K, H


def sha256(x):
    return compress(schedule(split512(convert(x))), K, H)