def is_all_vowels(s):
    harf = s.lower()
    vowel = "aeiou"
    for i in range(len(harf)):
        if(not harf[i] in vowel):
            return False
    return True
            
       
    
      








