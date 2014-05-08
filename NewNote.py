import sublime, sublime_plugin, datetime, string

class NewNoteCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.show_input_panel("Meeting Topic", "Quick description of the meeting", self.on_done, None, None)
    pass

  def on_done(self, text):
    view = self.window.new_file()
    view.run_command("insert_snippet", {"name": "Packages/Notes/NewNote.sublime-snippet"})
    view.run_command("insert", {"characters": text})
    view.run_command("next_field", {})
    view.run_command("insert_date_time", {})
    view.run_command("next_field", {})
    view.set_syntax_file("Packages/MarkdownEditing/Markdown (Standard).tmLanguage")
    file_name = datetime.datetime.now().strftime("%Y-%m-%d-")
    file_name = file_name + text.strip() + ".md"
    file_name = file_name.lower()
    file_name = file_name.replace(" ", "-")
    view.set_name(file_name)
