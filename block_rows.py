import sublime, sublime_plugin
# shift + super + 0

class BlockRowsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    region = self.view.sel()[0]
    if not region.empty():
      selected_area = self.view.substr(region)

      if ' do ' in selected_area:
        new_line = self.do_end_block(selected_area)
      else:
        new_line = self.brackets_block(selected_area, region)

      self.view.replace(edit, region, new_line)

  def do_end_block(self, selected_area):
    split       = selected_area.split('\n')
    first_part  = split[0].replace('\n', '').replace('do', '{').strip()
    second_part = split[1].replace('\n', '').strip()

    return first_part + ' ' + second_part + ' }'

  def brackets_block(self, selected_area, region):
    split              = selected_area.split('| ')
    first_part         = split[0].replace('{', 'do').strip() + '|'
    second_part        = split[1].replace('}', '').strip()
    startrow, startcol = self.view.rowcol(region.begin())
    spaces             = [" " for x in range(startcol)]

    return first_part + '\n' + ''.join(spaces) + '  ' + second_part + '\n' + ''.join(spaces) + 'end' + '\n'