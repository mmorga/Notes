# Notes Sublime Text Plugin

This is a simple plugin that provides the ability to:

* Insert a date/time stamp.
* Create a new markdown file formatted to take notes in.

The new file functionality prompts for a topic, then uses the topic to set the title for the notes file and sets a name for the file using the format:

`YYYY-MM-DD-topic-lowercase-with-dashes.md`

The file itself uses a Sublime snippet to create a file that looks like this:

```markdown
# Topic

Thu, May 08, 2014, 03:53 PM

Project: _____

## Who

_____

## Notes

$0
```

The main header is populated with the user input. The Project and Who are snippet fields that you can tab between.

The settings file lets you change the time format to the format you'd like.

