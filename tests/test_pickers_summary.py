
# Pickerr Summary test
#
# Checks the following functions return values for 
# pickers ( AICDPicker, FBPicker, KTPicker )
#
#
#      -- threshold
#      -- uncertanity
#      -- pick_ident
#      -- polarity
#  


from obspy import read as obspy_read

from phasepapy.phasepicker.aicdpicker import AICDSummary
from phasepapy.phasepicker.fbpicker import FBSummary
from phasepapy.phasepicker.ktpicker import KTSummary  

# picker summary

def test_picker_summary(event, picker):

   mseed = event + '_short.mseed'
   st = obspy_read(mseed,details=True)
   print (st)
   picker_class = picker().__class__.__name__
   picker_index = picker_class.index('Picker')
   picker_summary_class = picker_class[:picker_index] + 'Summary'

   for s in st[:2]:
      print (s)
      picket_summary_str = picker_summary_class + \
                           '(' + 'picker(),' + 's)'
      picker_summary = eval(picket_summary_str)
      
      threshold = picker_summary.threshold()
      print ( 'threshold = ',threshold )
      assert len(threshold) > 0

      uncertanity = picker_summary.uncertainty()
      print ( 'uncertainity = ', uncertanity )
      assert len(uncertanity) >= 0

      scnl, picks, trigger,snr = picker_summary.pick_ident()
      print ( 'scbl    = ',scnl )
      print ( 'picks   = ',picks)
      print ( 'trigger = ',trigger)
      print ( 'snr     = ',snr)
      assert len(picks) >= 0
      assert len(trigger) >= 0
      assert len(snr) >=0
  
      polarity = picker_summary.polarity()
      print ( 'Polarity    = ',polarity )
