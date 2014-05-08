import sublime, sublime_plugin, datetime

class InsertDateTimeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.settings = sublime.load_settings('Notes.sublime-settings')
    self.view.run_command("insert", {'characters': datetime.datetime.now().strftime(self.settings.get('datetime_format'))})
