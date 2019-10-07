import sublime, sublime_plugin

class BlockRowsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    region = self.view.sel()[0]
    if not region.empty():
      selected_area = self.view.substr(region)

      if ' do ' in selected_area:
        split         = selected_area.split('\n')
        first_part  = split[0].replace('\n', '').replace('do', '{').strip()
        second_part = split[1].replace('\n', '').strip()
        new_line    = first_part + ' ' + second_part + ' }'

      else:
        split       = selected_area.split('| ')
        first_part  = split[0].replace('{', 'do').strip() + '|'
        second_part = split[1].replace('}', '').strip()

        startrow, startcol = self.view.rowcol(region.begin())
        spaces    = [" " for x in range(startcol)]

        new_line    = first_part + '\n' + ''.join(spaces) + '  ' + second_part + '\n' + ''.join(spaces) + 'end' + '\n'

      self.view.replace(edit, region, new_line)