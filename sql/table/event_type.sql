DROP TABLE IF EXISTS event_type;

CREATE TABLE IF NOT EXISTS event_type (
 event_type_id serial primary key,
 code integer not null,
 description text not null UNIQUE);

INSERT INTO event_type
(code, description)
VALUES
 (0 , 'Unknown event' ),
 (1 , 'No event' ),
 (2 , 'Generic out' ),
 (3 , 'Strikeout' ),
 (4 , 'Stolen base' ),
 (5 , 'Defensive indifference'),
 (6 , 'Caught stealing' ),
 (7 , 'Pickoff error' ),
 (8 , 'Pickoff' ),
 (9 , 'Wild pitch' ),
 (10 , 'Passed ball' ),
 (11 , 'Balk' ),
 (12 , 'Other advance' ),
 (13 , 'Foul error' ),
 (14 , 'Walk' ),
 (15 , 'Intentional walk' ),
 (16 , 'Hit by pitch' ),
 (17 , 'Interference' ),
 (18 , 'Error' ),
 (19 , 'Fielder''s choice' ),
 (20 , 'Single' ),
 (21 , 'Double' ),
 (22 , 'Triple' ),
 (23 , 'Home run' ),
 (24 , 'Missing play' );