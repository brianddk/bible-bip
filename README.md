# Bible BIP39 Generator

This implements the widely flawed "security through obscurity" philosophy.  It will generate a BIP39 seed that can be obscured into Bible passages with a set of word offsets.  Simply run the script and it will grind through BIP39 seeds until it finds a seed that can be found in the King James Bible.  Since this set of seeds is smaller than the unrestricted set of all BIP39 seeds it will reduce the entropy from 2^128 to 2^122 for a twelve word seed.  Twenty-four word seeds would likewise be reduced from 2^256 to 2^244.  For most all use cases, this should still be plenty.

I choose to use the King James Bible since the text has remained largely unchanged for the last 400 years, and will likely stay constant for the next 400 years.  You can get a much better "hit rate" in something like The New International Version Bible, but the that edition has changed the text in 1973, 1978, 1984, and 2011.  So there is a small chance that one of the versions will properly encode a seed where another may not.  This was my may reasoning for choosing KJV over NIV.

The script will produce three things to record:

1. A set of ordered Bible verses
2. The word offset into each of the ordered verses
3. The original BIP39 seed this is encoding

Example:

    1. Job 39:8
    2. Deuteronomy 28:61
    3. Leviticus 18:12
    4. First Chronicles 4:4
    5. Genesis 2:22
    6. Ezekiel 42:5
    7. Deuteronomy 28:44
    8. Deuteronomy 19:15
    9. Daniel 1:4
    10. Judges 9:9
    11. Second Kings 11:11
    12. Joshua 9:13

    word offsets: 2 3 4 2 3 3 3 2 1 3 3 3

    seed: range sick uncover pen rib upper lend witness child olive guard bottom

For example `range` is encoded in Book: Job; Chapter: 39; Verse: 8; Word: 2

    Job 39:8 - The RANGE of the mountains is his pasture...

Note that since BIP39 words are four-character unique, the matching is only concerned with the first three to four letters.  So in our example, `pen` is matched with the first three characters of the second word of First Chronicles 4:4

    1 Chronicles 4:4 - And PENuel the father of Gedor...

Someone finding a list of bible verses might not immediately assume that this is a BIP39 seed and might just think it's a bible study list.  Though it is important that you keep the order straight.  Mixing the order could be fatal for 24 word seeds, though mixed order 12 word seeds could still be reassembled with a bit of work.

The verses are specifically chosen to try to have the word offsets as close to the beginning of the verse as possible.  This adds some convince and makes the `offsets` list somewhat optional.  Though loosing the offsets will require you to do some brute force attempts to eventually reassemble your key.  Best to keep it around, but the list of 12 numbers could be seen as innocuous as a list of Bible verses.

Of course this could also be done with the Quran, Tipitaka, Vedas, Torah, or any other text. It's just easy to get a text KJV Bible and I'm somewhat familiar with the verse notations.
