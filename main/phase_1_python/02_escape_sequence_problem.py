letter = '''
        Dear <|Name|>
        You are selected
        <|Date|>
        '''

print(letter.replace('<|Name|>', "aditya").replace("<|Date|>", "06 september 2050"))