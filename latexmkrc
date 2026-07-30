# Project-local TeX inputs. Keep main independent of external analysis projects.
$ENV{'TEXINPUTS'} = './utils//:./slides//:./:' . ($ENV{'TEXINPUTS'} || '');
