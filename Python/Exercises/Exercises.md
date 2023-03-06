Exercises
---------
1. Create approved file of the first 30 days
2. Refactor the UpdateQuality method ( else-if / match-case ) 
3. Define derived classes from StoredItem class and encapsulate the update functionality
4. Define a factory class that creates the StoredItems based on their names
5. Add Conjured item support

We have recently signed a supplier of "Conjured" items. This requires AN UPDATE to our system:
"Conjured" items degrade in Quality twice as fast as normal items.

Feel free to make any changes to the UpdateQuality method and add any new code as long as everything still works correctly. 
However, do not alter the Untouchable definitions as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code ownership 
       
6. Add notification support

Our new notification service lets shoppers know that items were updated. When StoredItems are updated they can leave a message to be sent to the town crier.
Update the UpdateQuality to send the message if it was updated. Create a mock notification service that logs the sent messages and add a verification in the tests for that log.
	

Hints (examples):
Extract methods
Guard statements
Invert ifs
Duplicate and insert conditions
