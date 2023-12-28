def prepare_data():
    data = []
    file = open('input', 'r').read().splitlines()

    for line in file:
        record, checksum_str = line.split()
        checksum = [int(n) for n in checksum_str.split(',')]
        data.append((record, checksum))

    return data

def calculate_arrangements(data):
    total_arrangements = 0

    for record, checksum in data:
        valid_positions = {0: 1}

        for i, contigous_length in enumerate(checksum):
            new_valid_positions = {}

            for position, count in valid_positions.items():
                new_positions_within_bounds = range(position, len(record) - sum(checksum[i + 1:]) + len(checksum[i + 1:]))

                for new_pos in new_positions_within_bounds:
                    is_contiguous_valid = (
                        new_pos + contigous_length - 1 < len(record) and '.' not in record[new_pos:new_pos + contigous_length]
                    )

                    is_last_checksum = i == len(checksum) - 1 and '#' not in record[new_pos + contigous_length:]

                    is_not_last_checksum = i < len(checksum) - 1 and new_pos + contigous_length < len(record) and record[new_pos + contigous_length] != '#'

                    if is_contiguous_valid and (is_last_checksum or is_not_last_checksum):
                        new_valid_positions[new_pos + contigous_length + 1] = new_valid_positions.get(new_pos + contigous_length + 1, 0) + count

                    if record[new_pos] == '#':
                        break

            valid_positions = new_valid_positions

        total_arrangements += sum(valid_positions.values())

    return total_arrangements

def main():
    data = prepare_data()
    arrangements = calculate_arrangements(data)
    print(arrangements)


if __name__ == '__main__':
    main()