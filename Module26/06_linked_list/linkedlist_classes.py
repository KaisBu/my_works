class Knot:
    def __init__(self, data=None, next_link=None) -> None:
        self.data = data
        self.next_link = next_link

    def __str__(self) -> str:
        return '{data}'.format(data=self.data)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def __str__(self) -> str:
        if self.head:
            cur_knot = self.head
            all_data = [str(cur_knot.data)]
            while cur_knot.next_link:
                cur_knot = cur_knot.next_link
                all_data.append(str(cur_knot.data))
            return '[{data}]'.format(data=' '.join(all_data))
        return 'LinkedList []'

    def append(self, data) -> None:
        new_knot = Knot(data)
        self.length += 1

        if not self.head:
            self.head = new_knot
            return
        last_knot = self.head
        while last_knot.next_link:
            last_knot = last_knot.next_link
        last_knot.next_link = new_knot

    def get(self, index) -> None:
        last_knot = self.head
        knot_index = 0

        while knot_index <= index:
            if knot_index == index:
                return last_knot.data
            knot_index += 1
            last_knot = last_knot.next_link

    def remove(self, index) -> None:
        head_knot = self.head
        knot_index = 0

        if self.length == 0 or self.length < index:
            raise IndexError
        elif head_knot:
            if index == 0:
                self.head = head_knot.next_link
                self.length -= 1
                return

            while head_knot:
                knot_index += 1
                last_knot = head_knot
                head_knot = head_knot.next_link

                if knot_index == index:
                    last_knot.next_link = head_knot.next_link
                    self.length -= 1
                    return
