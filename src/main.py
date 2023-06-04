from RdfTemplater import RdfTemplater


def main():
    input = "sakjd <<LN(rdf:PP, LN('2 ','3n',LN('4',/id)), 6E10, URL_ENCODE('@@', /jj))>>543 5 ew <<LN('w', LN(/gary))>>"
    input = \
    """
    dsa dasd<Lhjkhkj<<LN(/gary)>>
    
    sdifjldsk
    
    << if /jjk >>
    asd <<LN(/jjk)>>
    <<endif>>
    
    <<if /jjk>>
    asdrrrrrrrrrrrrrrrrrrrrr<<LN(/jjk)>>
    <<endif>>
    sdfhj
    
    ajksadl
    """
    templater = RdfTemplater(input)
    out = templater.apply({'id':111, 'jjk': "k", "gary": 'grrr'})
    print(out)
   # Functions.__dict__.get("LN")(*[1,2,7][::-1])





if __name__ == '__main__':
    main()


