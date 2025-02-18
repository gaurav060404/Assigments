class SpellNotFoundError(Exception):
    pass

class DarkMagicError(Exception):
    pass

class BlankSpellError(Exception):
    pass

def cast_spell(spellbook, spell_name):
    try:
        if spell_name not in spellbook:
            raise SpellNotFoundError(f"ERROR: The spell '{spell_name}' is missing from the spellbook!")
        elif spell_name == "Forbidden Magic" or spell_name == "Avadacadabra":
            raise DarkMagicError("ERROR: You cannot cast Forbidden Magic! It's too dangerous!")
        elif spell_name.strip() == "":
            raise BlankSpellError("ERROR: You tried to cast an empty spell. Be careful!")

        print(f"Casting {spell_name}: {spellbook[spell_name]}")

    except (SpellNotFoundError, DarkMagicError, BlankSpellError) as e:
        print(e)

spellbook = {
    "Wingardium Leviosa": "With this charm a witch or wizard can make things fly with the flick of a wand",
    "Healing Light": "A warm light heals your wounds.",
    "Teleport": "You vanish and reappear somewhere else.",
    "Avadacadabra" : "One of the unforgivable curses/spells which kills your target."
}

cast_spell(spellbook, "Wingardium Leviosa")  
cast_spell(spellbook, "Shadow Step")
cast_spell(spellbook, "Avadacadabra")  
cast_spell(spellbook, "")  
