import xml.etree.ElementTree as ET
import re

tree = ET.parse("cluster_standalone_listview.xml")
root = tree.getroot()
root_tag = root.tag
print(root_tag)

xml_root = ET.fromstring(tree)
print(xml_root)
profile="""
    SymCLI_ML
        Symmetrix
            Symm_Info
                symid = dataset:sid    
"""

profile_input = profile

def parse_using_profile(xml_data, profile_input):
    """Expands the supplied profile to a python data structure"""

    # ------------------------------------------------------------------------------
    #   Declare the Indentation History as starting at 0
    # ------------------------------------------------------------------------------
    indentation_history = [0]

    # ------------------------------------------------------------------------------
    #   Profile holders
    # ------------------------------------------------------------------------------
    complex_profile = {}
    complex_profile_history = [complex_profile]
    current_profile_position = complex_profile_history[-1]

    # ------------------------------------------------------------------------------
    #   Capture available tokens from the profile input using a carriage return
    #   as a separator
    # ------------------------------------------------------------------------------
    tokens = profile_input.split('\n')

    # ------------------------------------------------------------------------------
    #   Process each token
    # ------------------------------------------------------------------------------
    for token in tokens:

        # ------------------------------------------------------------------------------
        #   Declare holders for the length_indentation and token_data
        # ------------------------------------------------------------------------------
        length_indentation = None
        token_data = None

        # ------------------------------------------------------------------------------
        #   Attempt to match token with indentation
        # ------------------------------------------------------------------------------
        match = re.search('(\s+)(.*)', token)  # pylint: disable=W1401

        # ------------------------------------------------------------------------------
        #   If a match is found capture the indentation and the token_data
        # ------------------------------------------------------------------------------
        if match:
            length_indentation = len(match.group(1))
            token_data = match.group(2).strip()
        # ------------------------------------------------------------------------------
        #   Otherwise mark the indentation as 0 and remove any carriage returns from
        #   the token_data
        # ------------------------------------------------------------------------------
        else:
            length_indentation = 0
            token_data = token.strip()

        # ------------------------------------------------------------------------------
        #   If token data is available
        # ------------------------------------------------------------------------------
        if token_data:

            # ------------------------------------------------------------------------------
            #   Store the previous_indentation information
            # ------------------------------------------------------------------------------
            previous_indentation = indentation_history[-1]

            # ------------------------------------------------------------------------------
            #    If the indentation has increased, store the indentation in the history
            # ------------------------------------------------------------------------------
            if length_indentation > previous_indentation:
                indentation_history.append(length_indentation)

            # ------------------------------------------------------------------------------
            #    Otherwise if the indentation has decreased
            # ------------------------------------------------------------------------------
            elif previous_indentation > length_indentation:

                # ------------------------------------------------------------------------------
                #    Step back through the indentation
                # ------------------------------------------------------------------------------
                while previous_indentation > length_indentation:
                    indentation_history.pop()
                    previous_indentation = indentation_history[-1]

                    # ------------------------------------------------------------------------------
                    #    ... And the associated history
                    # ------------------------------------------------------------------------------
                    complex_profile_history.pop()
                    current_profile_position = complex_profile_history[-1]

            # ------------------------------------------------------------------------------
            #    If the token contains a value ( signified by an = sign )
            # ------------------------------------------------------------------------------
            if '=' in token_data:

                # ------------------------------------------------------------------------------
                #    Capture the key and the record_holder
                # ------------------------------------------------------------------------------
                key, record_holder = token_data.split('=')

                # ------------------------------------------------------------------------------
                #    Remove leading and ending space using strip() for the key and record_holder
                # ------------------------------------------------------------------------------
                key = key.strip()
                record_holder = record_holder.strip()

                # ------------------------------------------------------------------------------
                #    Check for an Ignore marker
                # ------------------------------------------------------------------------------
                if record_holder == '__IGNORE__':

                    if key not in current_profile_position:
                        current_profile_position[key] = {}

                    current_profile_position[key]['__IGNORE__'] = 1

                # ------------------------------------------------------------------------------
                #    Otherwise continue
                # ------------------------------------------------------------------------------
                else:

                    # ------------------------------------------------------------------------------
                    #    Split unprocessed records
                    # ------------------------------------------------------------------------------
                    records_unprocessed = record_holder.split(' ')

                    # ------------------------------------------------------------------------------
                    #    Capture New Dataset markers where available
                    # ------------------------------------------------------------------------------
                    if key == '__NEW_DATASET__':
                        current_profile_position['__NEW_DATASET__'] = records_unprocessed

                    # ------------------------------------------------------------------------------
                    #    Otherwise Capture External Values where available
                    # ------------------------------------------------------------------------------
                    elif key == '__EXTERNAL_VALUE__':
                        current_profile_position['__EXTERNAL_VALUE__'] = records_unprocessed

                    # ------------------------------------------------------------------------------
                    #    Otherwise Capture New External Values where available
                    # ------------------------------------------------------------------------------
                    elif key == '__NEW_EXTERNAL_VALUE_HOLDER__':
                        current_profile_position['__NEW_EXTERNAL_VALUE_HOLDER__'] = records_unprocessed

                    # ------------------------------------------------------------------------------
                    #    Otherwise Capture Processing markers where available
                    # ------------------------------------------------------------------------------
                    elif key == '__DATASET_PROCESSING__':
                        current_profile_position['__DATASET_PROCESSING__'] = records_unprocessed

                    # ------------------------------------------------------------------------------
                    #    Otherwise Capture Always Follow markers where available
                    # ------------------------------------------------------------------------------
                    elif key == '__ALWAYS_FOLLOW__':
                        current_profile_position['__ALWAYS_FOLLOW__'] = records_unprocessed

                    # ------------------------------------------------------------------------------
                    #    Otherwise ....
                    # ------------------------------------------------------------------------------
                    else:

                        # ------------------------------------------------------------------------------
                        #    Add an order processing sequence to the profile, create where necessary
                        #    or append
                        # ------------------------------------------------------------------------------
                        if '__order__' not in current_profile_position:
                            current_profile_position['__order__'] = [key]
                        else:
                            current_profile_position['__order__'].append(key)

                        # ------------------------------------------------------------------------------
                        #    Process records_unprocessed
                        # ------------------------------------------------------------------------------
                        for record_unprocessed in records_unprocessed:

                            # ------------------------------------------------------------------------------
                            #    Add the key
                            # ------------------------------------------------------------------------------
                            if key not in current_profile_position:
                                current_profile_position[key] = {}

                            # ------------------------------------------------------------------------------
                            #    Create the record holder or append a new record
                            # ------------------------------------------------------------------------------
                            if '__record__' not in current_profile_position[key]:
                                current_profile_position[key]['__record__'] = [{}]
                            else:
                                current_profile_position[key]['__record__'].append({})

                            # ------------------------------------------------------------------------------
                            #    Process each record
                            # ------------------------------------------------------------------------------
                            for record in record_unprocessed.split(','):
                                record_key, record_value = record.split(':')
                                current_profile_position[key]['__record__'][-1][record_key] = record_value

            # ------------------------------------------------------------------------------
            #    If the token does not contain an = sign
            # ------------------------------------------------------------------------------
            else:

                # ------------------------------------------------------------------------------
                #    Create a named dictionary
                # ------------------------------------------------------------------------------
                holder = {}

                # ------------------------------------------------------------------------------
                #    Store the named dictionary as the current token
                # ------------------------------------------------------------------------------
                current_profile_position[token_data] = holder

                # ------------------------------------------------------------------------------
                #    Add an order processing sequence
                # ------------------------------------------------------------------------------
                if '__order__' not in current_profile_position:
                    current_profile_position['__order__'] = [token_data]
                else:
                    current_profile_position['__order__'].append(token_data)

                # ------------------------------------------------------------------------------
                #    Update the current position to the named dict
                # ------------------------------------------------------------------------------
                current_profile_position = holder

                # ------------------------------------------------------------------------------
                #    Add to the current history
                # ------------------------------------------------------------------------------
                complex_profile_history.append(holder)

    # ------------------------------------------------------------------------------
    #    Return the complex profile
    # ------------------------------------------------------------------------------
    return complex_profile