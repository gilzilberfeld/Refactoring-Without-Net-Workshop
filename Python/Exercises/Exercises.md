Exercises
---------

Feel free to make any changes to the **GildedRose** class, and add any new code, as long as everything still works correctly. 
However, do not alter the **Dependencies** class definitions as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code ownership. 
The original Gilded Rose requirements are [here](..\\GildedRoseExercise\\GildedRoseReqs.md).

1. Create an approval file of the first 30 days
2. Refactor the UpdateQuality method ( else-if / match-case ) 
3. Define derived classes from StoredItem class and encapsulate the update functionality.

Note: The goblin allows changing the **StoredItem** class. We came to an agreement.

4. Define a factory class that creates the **StoredItems** based on their names

We have recently signed a supplier of *Conjured* items. This requires AN UPDATE to our system:
 
5. Add *Conjured* items support (they contain "Conjured" in their name)

*Conjured* items degrade in Quality twice as fast as normal items.
       
6. Add notification support

Our new notification service lets shoppers know that items were updated. 
When **StoredItems** are updated, they can leave a message to be sent to the town crier.
Update **GildedRose** class to accept a notifier, and the **UpdateQuality** method to send the message, if it was updated. 
Create a mock notification service that logs the sent messages and add a verification in the tests for that log.
	
