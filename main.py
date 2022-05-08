from operator import mod
import random

modes = [
    'Natural Minor',
    'Major',
    'Harmonic Minor',
    'Melodic Minor',
    'Dorian',
    'Phrygian',
    'Lydian',
    'Mixolydian',
    'Major Pentatonic',
    'Minor Pentatonic',
    'Whole Tone',
    'WH Diminished',
    'HW Diminished',
    'Bebop Minor',
    'Blues',
    'Locrian']

keys = [
    'C',
    'C#/Db',
    'D',
    'Eb',
    'E',
    'F',
    'F#/Gb',
    'G',
    'Ab',
    'A',
    'Bb',
    'B/Cb']

# C Natural Minor

def pick_two_random (xs, ys):
  x = random.choice(xs)
  y = random.choice(ys)

  return f"{x} {y}"

print(pick_two_random(keys, modes))
print(pick_two_random(keys, modes))
print(pick_two_random(keys, modes))
print(pick_two_random(keys, modes))
print(pick_two_random(keys, modes))

answer = pick_two_random(keys, modes)
print(answer)
