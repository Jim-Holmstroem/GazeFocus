import subprocess
import operator

class WInfo():
    def __init__(self,raw_information):
        raw_information=raw_information.split()
        self.id=raw_information[0]
        self.points = raw_information[1:7]
        self.title = reduce(lambda l,r:l+' '+r,raw_information[7:]) #the leftovers are the title of the window
    
    def __str__(self):
        return 'WInfo<'+self.title+'/'+self.id+'>'+str(self.points)

    def focus_me(self):
        output=subprocess.check_output(['wmctrl','-i','-a',self.id])

def is_valid(winfo):
    baseprogram_list=['N/A Dash', 'N/A panel','N/A launcher','N/A DNDCollectionWindow'] 
    is_baseprogram=any(map(lambda title:winfo.title.find(title)!=-1,baseprogram_list))
    return not is_baseprogram and True #perhaps more things to make it an invalid window

class WLayoutInfo():
    def __init__(self):
        """
        Creates the current layout given from wmctrl
        NOTE creates the layout from when its called
        """
        self.winfos=filter(is_valid,map(WInfo,subprocess.check_output(['wmctrl', '-pGl']).splitlines()))

    def focus_the_highest_window_at(self,at):
        """
        Focuses the first window located at position 'at'
        """
        pass

    def __getitem__(self,i):
        return self.winfos[i]
    def __str__(self):
        return reduce(lambda l,r:l+', '+r,map(str,self.winfos))

def main():
    
    wlayout=WLayoutInfo()
    for p in wlayout:
        print p
    wlayout[3].focus_me()

if __name__=='__main__':
    main()

